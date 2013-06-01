dojo.require("esri.map");
var map;
function init (){
	map = new esri.Map("mapDiv", {
		center: [-56.049, 38.485],
		zoom: 3,
		basemap: "streets"
	});
}
dojo.ready(init);	