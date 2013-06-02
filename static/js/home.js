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

        	//Make these explicit first.
        	$("#chart_race").show();
        	$("#chart_sex").hide();
        	$("#chart_age").hide();  	

            //create the popup so we can specify that the popupWindow option is false. Additional options
            //can be defined for the popup like modifying the highlight symbol, margin etc. 
            var popup = Popup({
                popupWindow: false
            }, domConstruct.create("div"));

		    var map = new Map("mapDiv", {
		        basemap:"topo",
		        center:[-104.9,39.7392], //long, lat
		        zoom:7,
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

		    //When a CLICK occurs on the map...
		    featureLayer.on("click", function(event){
		    	var info = {};
		    	//info ["area_code"] = event.graphic.attributes ["Area"];
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

		    	//Update the Representative & Demographic info.
		    	$("#rep").html(info["rep"]);
		    	$("#party").html(info["party"]);
		    	$("#web_link").html("<a href='" + info["web_link"] + "'>" + info["web_link"] + "</a>");
		    	$("#state").html(info["state"]);
		    	$("#district").html(info["district"]); 

		    	//AJAX GET: Total Population.
			  	$.ajax({
				    type:"GET",
				    url:URL_TOTAL_POP,
				    data: {"district":info["district"], "state":info["state"]},
				      success: function(data){
				      	var totalPop = data ["POP_TOTAL"]
				      	$("#total_pop").html(totalPop[0]);		
				      },
				      error: function(data){
				        alert("An unexpected error occurred when retrieving data. Please try again."); 
				      }
				  });

		    	//AJAX GET: Sex Breakdown of Population.
			  	$.ajax({
				    type:"GET",
				    url:URL_POP_SEX,
				    data: {"district":info["district"], "state":info["state"]},
				      success: function(data){
				      	draw_the_chart("chart_sex", "Sex of Population", "Sex", "Population", data);
				      },
				      error: function(data){
				        alert("An unexpected error occurred when retrieving data. Please try again."); 
				      }
				  });

		    	//AJAX GET: Age Breakdown of Population.
			  	$.ajax({
				    type:"GET",
				    url:URL_POP_AGE_DEC,
				    data: {"district":info["district"], "state":info["state"]},
				      success: function(data){
				      	draw_the_chart("chart_age", "Age of Population", "Age", "Population", data);
				      },
				      error: function(data){
				        alert("An unexpected error occurred when retrieving data. Please try again."); 
				      }
				  });

		    	//AJAX GET: Race Breakdown of Population.
			  	$.ajax({
				    type:"GET",
				    url:URL_POP_RACE_ANY,
				    data: {"district":info["district"], "state":info["state"]},
				      success: function(data){
				      	draw_the_chart("chart_race", "Race of Population", "Race", "Population", data);
				      },
				      error: function(data){
				        alert("An unexpected error occurred when retrieving data. Please try again."); 
				      }
				  });
		    });

		    map.addLayer(featureLayer);
		    window.map = map;		    

		  /** Google Charting API function from: https://google-developers.appspot.com/chart/interactive/docs/quick_start **/
		  /** The function assumes that the data payload is a list with 2-tuples of (String, [Number, String]) **/
	      function draw_the_chart(html_id, title, xaxis_label, yaxis_label, data) {		

		        // Create the data table.
		        var data_table = new google.visualization.DataTable();
		        data_table.addColumn('string', xaxis_label);
		        data_table.addColumn('number', yaxis_label);

		        //Populate a list containing all key-value pairs.
		        var datalist = [];
		        $.each (data, function(key, value){
		        	var val = parseInt(value[0])
		        	var pretty_key = value[1]
		        	datalist.push([pretty_key, val]);
		        });
		        data_table.addRows(datalist);

		        // Set chart options
		        var options = {'title': title,
		        			chartArea:{"left":30},
		        			height:550,
		        			pieSliceText:"none",
		        			width:500,
		                   	legend: {'position':'left'}};

		        // Instantiate and draw our chart, passing in some options.
		        var chart = new google.visualization.PieChart(document.getElementById(html_id));
		        chart.draw(data_table, options);
	      	}		    
        });
    });


//Some event-handling via JQuery.
$(document).ready(function(){

	$("#next").click(function(){
		var visibleChart = $("#chart_container .charts:visible");
		visibleChart.hide();
		var nextToShow = $(visibleChart).next(".charts:hidden");
		if (nextToShow.length > 0)
			nextToShow.show();
		else
			$("#chart_container .charts:hidden:first").show();

	});

	$("#previous").click(function(){
		var visibleChart = $("#chart_container .charts:visible");
		visibleChart.hide();
		var nextToShow = $(visibleChart).prev(".charts:hidden");
		if (nextToShow.length > 0)
			nextToShow.show();
		else
			$("#chart_container .charts:hidden:last").show();

			
	});

});
















//@ sourceURL=home.js
