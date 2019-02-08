// Function to determine marker radius based on price
function markerSize(price) {
    return price / 40;
  }

var streetmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 8,
    id: "mapbox.streets",
    accessToken: API_KEY //"pk.eyJ1IjoibWFydGluYW1hZ2R5IiwiYSI6ImNqcjNtMXI3czFtdWozeWxzbm1kbDFoankifQ.xpWlsJKz-XqoIiRipPeioA" 
});

// Define arrays to hold created city and state markers
var stateMarkers_2013 = [];
var stateMarkers_2014 = [];
var stateMarkers_2015 = [];
var stateMarkers_2016 = [];
var stateMarkers_2017 = [];
var stateMarkers_2018 = [];

var url ='/cities';
// An array containing all of the information needed to create city and state markers
d3.json(url).then(function(data){
  var dKeys = Object.keys(data);

  // Loop through locations and create city and state markers for 2013
  for (var i = 0; i < dKeys.length; i++) {
    var latLng = data[dKeys[i]]['Coordinates'].split(",");
    stateMarkers_2013.push(
        L.circle([parseInt(latLng[0]), parseInt(latLng[1])], {
        stroke: false,
        fillOpacity: 0.7,
        color: "#0D3D56",
        radius: markerSize(data[dKeys[i]]['Average (Median) Sale Price Per Year']['2013'])
        })
      );
    }

  // Loop through locations and create city and state markers for 2014
  for (var i = 0; i < dKeys.length; i++) {
      var latLng = data[dKeys[i]]['Coordinates'].split(",");
  stateMarkers_2014.push(
    L.circle([parseInt(latLng[0]), parseInt(latLng[1])], {
      stroke: false,
      fillOpacity: 0.7,
      color: "#1496BB",
      radius: markerSize(data[dKeys[i]]['Average (Median) Sale Price Per Year']['2014'])
      })
    );
  }
  
  // Loop through locations and create city and state markers for 2015
  for (var i = 0; i < dKeys.length; i++) {
    var latLng = data[dKeys[i]]['Coordinates'].split(",");
    stateMarkers_2015.push(
      L.circle([parseInt(latLng[0]), parseInt(latLng[1])], {
        stroke: false,
        fillOpacity: 0.7,
        color: "#829356",
        radius: markerSize(data[dKeys[i]]['Average (Median) Sale Price Per Year']['2015'])
        })
      );
    }
    
  // Loop through locations and create city and state markers for 2016
  for (var i = 0; i < dKeys.length; i++) {
    var latLng = data[dKeys[i]]['Coordinates'].split(",");
    stateMarkers_2016.push(
      L.circle([parseInt(latLng[0]), parseInt(latLng[1])], {
        stroke: false,
        fillOpacity: 0.7,
        color: "#BCA126",
        radius: markerSize(data[dKeys[i]]['Average (Median) Sale Price Per Year']['2016'])
        })
      );
    }
    
  // Loop through locations and create city and state markers for 2017
  for (var i = 0; i < dKeys.length; i++) {
    var latLng = data[dKeys[i]]['Coordinates'].split(",");
    stateMarkers_2017.push(
      L.circle([parseInt(latLng[0]), parseInt(latLng[1])], {
        stroke: false,
        fillOpacity: 0.7,
        color: "#F26D21",
        radius: markerSize(data[dKeys[i]]['Average (Median) Sale Price Per Year']['2017'])
        })
      );
    }
    
  // Loop through locations and create city and state markers for 2018
  for (var i = 0; i < dKeys.length; i++) {
    var latLng = data[dKeys[i]]['Coordinates'].split(",");
    stateMarkers_2018.push(
      L.circle([parseInt(latLng[0]), parseInt(latLng[1])], {
        stroke: false,
        fillOpacity: 0.7,
        color: "#C02F1D",
        radius: markerSize(data[dKeys[i]]['Average (Median) Sale Price Per Year']['2018'])
        })
      );
    }

  // Create two separate layer groups: one for cities and one for states
  var states_2013 = L.layerGroup(stateMarkers_2013);
  var states_2014 = L.layerGroup(stateMarkers_2014);
  var states_2015 = L.layerGroup(stateMarkers_2015);
  var states_2016 = L.layerGroup(stateMarkers_2016);
  var states_2017 = L.layerGroup(stateMarkers_2017);
  var states_2018 = L.layerGroup(stateMarkers_2018);
    
  // Create a baseMaps object
  var baseMaps = {
    "Satelite Map": streetmap
  };

  // Create an overlay object
  var overlayMaps = {
    "2018": states_2018,
    "2017": states_2017,
    "2016": states_2016,
    "2015": states_2015,
    "2014": states_2014,
    "2013": states_2013
  };
  var myMap = L.map("map", {
    center: [37.09, -95.71],
    zoom: 4,
    layers: [streetmap, states_2018] //, states_2017, states_2016, states_2015, states_2014, states_2013]
  });
  
  // Pass our map layers into our layer control
  // Add the layer control to the map
  L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
  }).addTo(myMap);


  // Add legend to map
  let legend = L.control({position: 'bottomright'});

  legend.onAdd = function() {
    let div = L.DomUtil.create('div', 'info legend'),
    labels = [2013, 2014, 2015, 2016, 2017, 2018],
    colors = ["#0D3D56", "#1496BB", "#829356", "#BCA126", "#F26D21", "#C02F1D"];

    for(let i = 0; i < colors.length; i++) {
      div.innerHTML +=
        '<i style="background:' + colors[i] + '"></i> ' +
        (labels[i] ? labels[i] + '<br>' : '+');
    }
    return div;
  };
  legend.addTo(myMap);

});