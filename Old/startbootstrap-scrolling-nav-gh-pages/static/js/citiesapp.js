   function buildCharts(city) {
       console.log("building charts")
    var url = `/cities`;
    // Build line chart displaying the average sales per year for the past x years
    d3.json(url).then(function(data){
        //city = 'Austin, TX'
        var years = []
        var amounts = []
        console.log("City Details")
        console.log(data[city]);
        var dKeys = Object.keys(data[city]);
        console.log(dKeys)

        var details = data[city][dKeys[0]]
        console.log("Details")
        console.log(details)

        var years = Object.keys(details)
        console.log("Years")
        console.log(years)

        for (i = 0; i < (years.length) ; i++) {
            var year = years[i]
            amounts.push(details[years[i]]);
          }
          console.log(amounts)
       var trace2 = [{
          x: years,
          y: amounts,
          //labels: ?,
          //"hovertext": labels,
          type: 'line'
        }];
        var layout2 = {
        title: `Average Sales Per Year in ${city}`
        };
        Plotly.newPlot('line', trace2, layout2);   //<- is there a div for each visualization?
    }).catch((error) => {
      console.log("Error: " + error);
    });  
                                                        
  }
  
  function init() {
          //dropdown select year
    // Grab a reference to the dropdown select element
    var selector2 = d3.select("#selcity");

    // Use the list of sample names to populate the select options
        d3.json("/names").then((cities)=>{
          console.log("mart",cities);
        cities.forEach((city) => {
        selector2
            .append("option")
            .text(city)
            .property("value", city);
        });


    // Use the first sample from the list to build the initial plots
    const firstcity = cities[0];
    buildCharts(firstcity);
    });
  };  //});
  
  
  function optionChanged(newCity) {
  // Fetch new data each time a new sample is selected
  buildCharts(newCity);
  //buildMetadata(newCity);
  }
  
  // Initialize the dashboard
  init();
  //console.log("hewwo?")