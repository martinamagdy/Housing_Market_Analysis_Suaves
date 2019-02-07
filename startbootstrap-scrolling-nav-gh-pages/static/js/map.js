// Function to determine marker size based on population
function markerSize(population) {
    return population / 40;
  }

  var streetmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
      attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
      maxZoom: 8,
      id: "mapbox.streets",
      accessToken: API_KEY
  });

  // Define arrays to hold created city and state markers
  var stateMarkers = [];

  var url ='/sale_price_2013_2018';
  // An array containing all of the information needed to create city and state markers
  d3.json(url).then(function(data){

  // Loop through locations and create city and state markers
  for (var i = 0; i < data.locations.length; i++) {
  // Setting the marker radius for the state by passing population into the markerSize function
  console.log("fdfdfdf",data.locations[i].Coordinates);
  stateMarkers.push(
      L.circle(data.locations[i].Coordinates, {
      stroke: false,
      fillOpacity: 0.75,
      color: "purple",
      fillColor: "purple",
      radius: markerSize(data.locations[i]['city']['Median Sale Price Per Year']['2014'])
      })
    );
  }

  // Create two separate layer groups: one for cities and one for states
  var states = L.layerGroup(stateMarkers);
    
  // Create a baseMaps object
  var baseMaps = {
    "Satelite Map": streetmap
  };

  // Create an overlay object
  var overlayMaps = {
    "Housing price": states,
  };
  var myMap = L.map("map", {
    center: [37.09, -95.71],
    zoom: 5,
    layers: [streetmap, states]
  });
  
  // Pass our map layers into our layer control
  // Add the layer control to the map
  L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
  }).addTo(myMap);
});