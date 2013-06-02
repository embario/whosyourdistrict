    require([
        "dojo/ready", 
        "dojo/on",
        "dojo/_base/connect", 
        "dojo/dom",
        "dijit/registry",
        "dojo/dom-construct",
        "dojo/parser", 
        "dijit/layout/BorderContainer", 
        "dijit/layout/ContentPane", 
        "esri/map",
        "esri/arcgis/utils",
        "esri/domUtils",
        "esri/dijit/Popup",
        "esri/layers/FeatureLayer",
    	"esri/geometry/Extent",
    	"esri/InfoTemplate",
    ], function(
        ready, 
        on, 
        connect,
        dom,
        registry,
        domConstruct,
        parser, 
        BorderContainer, 
        ContentPane,
        Map,
        arcgisUtils,
        domUtils,
        Popup,
        FeatureLayer,
        Extent,
        InfoTemplate
    ) {
        ready(function(){

            parser.parse();

            //create the popup so we can specify that the popupWindow option is false. Additional options
            //can be defined for the popup like modifying the highlight symbol, margin etc. 
            var popup = Popup({
                popupWindow: false
            }, domConstruct.create("div"));

		    var map = new Map("mapDiv", {
		        basemap:"topo",
		        center:[-104.9,39.7392], //long, lat
		        zoom:9,
		        infoWindow: popup,
		        sliderStyle:"small"
		    });

		   	var url = "http://services1.arcgis.com/M8KJPUwAXP8jhtnM/arcgis/rest/services/ColoradoCongressionalDistricts/FeatureServer/0";
		    var template = new InfoTemplate("World Regions", "Region: ${REGION}");
		    var featureLayer = new esri.layers.FeatureLayer(url, {
		        id: "world-regions",
		        opacity:0.3,
		        infoTemplate: template,
		        outFields: ["*"]
		    });

		    featureLayer.on("click", function(event){
		    	var info = {};
		    	info ["area code"] = event.graphic.attributes ["Area"];
		    	info ["district"] = event.graphic.attributes["DISTRICT"];
		    	info ["district_id"] = event.graphic.attributes ["DistrictID"];
		    	info ["rep"] = event.graphic.attributes["REPRESENTA"];
		    	info ["party"] = event.graphic.attributes ["Party"];
		    	info ["web_link"] = event.graphic.attributes ["WEB_LINK"];
		    	info ["state"] = event.graphic.attributes ["State"];

		    	//Kludgy code here.
		    	var district = info["district"]
		    	if (info["district"].length == 1)
		    		var district = "0" + district
		    	info["district"] = district

		    	//Perform the AJAX GET Request.
			  	$.ajax({
				    type:"GET",
				    url:URL_TOTAL_POP,
				    data: {"district":info["district"], "state":info["state"]},
				      success: function(data){
				      	//Update Side Panel with new info.
				      	updatePanel(info);
				      },
				      error: function(data){
				        alert("An unexpected error occurred when retrieving data. Please try again."); 
				      }
				  });
		    });

		    map.addLayer(featureLayer);
		    window.map = map;		    

		    function updatePanel(info){

		    	label_areacode = "Area Code:";
		    	label_district = "District:";

		    	$('#infolist > tbody:last').append("<tr><td>" + label_areacode + "</td><td>" + 
		    		info["area_code"] + "</td></tr>");
		    	$('#infolist > tbody:last').append("<tr><td>" + label_district + "</td><td>" + 
		    		info["district"] + "</td></tr>");		    	
		    }

            function initializeSidebar(map){
                var popup = map.infoWindow;

                //when the selection changes update the side panel to display the popup info for the 
                //currently selected feature. 
                connect.connect(map, "onClick", function(){
                	alert("HEYYY");
                    //displayPopupContent(popup.getSelectedFeature());
                });

                //when the selection is cleared remove the popup content from the side panel. 
                connect.connect(popup, "onClearFeatures", function(){
                    //dom.byId replaces dojo.byId
                    dom.byId("featureCount").innerHTML = "Congressional District";
                    //registry.byId replaces dijit.byId
                    registry.byId("leftPane").set("content", "");
                    domUtils.hide(dom.byId("pager"));
                });

                //When features are associated with the  map's info window update the sidebar with the new content. 
                connect.connect(popup, "onSetFeatures", function(){
                    displayPopupContent(popup.getSelectedFeature());
                    dom.byId("featureCount").innerHTML = popup.features.length + " feature(s) selected";

                    //enable navigation if more than one feature is selected 
                    popup.features.length > 1 ? domUtils.show(dom.byId("pager")) : domUtils.hide(dom.byId("pager"));
                });
            }

            function displayPopupContent(feature){
                if(feature){
                	debugger;
                    var content = feature.getContent();
                    registry.byId("leftPane").set("content", content);
                }
            }
        });
    });

//@ sourceURL=home.js