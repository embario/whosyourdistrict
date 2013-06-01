require([ "dojo/dom-construct",
    	"esri/map",
    	"esri/layers/FeatureLayer",
    	"esri/geometry/Extent",
    	"esri/InfoTemplate",
    	"dojo/domReady!"], 
    	
	function(domConstruct, Map, FeatureLayer, Extent, InfoTemplate) {

	    var map = new Map("mapDiv", {
	        basemap:"topo",
	        center:[-104.9,39.7392], //long, lat
	        zoom:9,
	        sliderStyle:"small"
	    });

	    var url = "http://maps1.arcgisonline.com/ArcGIS/rest/services/USA_Congressional_Districts/MapServer/2";
	    var template = new InfoTemplate("World Regions", "Region: ${REGION}");
	    var fl = new FeatureLayer(url, {
	        id: "world-regions",
	        opacity:0.5,
	        infoTemplate: template
	    });

	    map.addLayer(fl);
	}
);