//function to build bar chart that show price per square foot for each city
function barcity(year){
    url='/cities';
    d3.json(url).then(function(data){
        var price_sqft=[]
        var cities=[]
        //get square foot price for each city in that year
        for(i in data){
            cities.push(i);
            price_sqft.push(data[i]["Median Price Per Square Foot"][`${year}`]);   
        }
        console.log("price",price_sqft);
        console.log("city",cities);
        // Trace1 for the price per sq ft data
        var trace1 = [{
            x: price_sqft,
            y: cities,
            name: "Price Per Sqft",
            text: price_sqft,
            textposition: 'auto',
            type: "bar",
            orientation: "h"
        }];
        
        // Apply the group bar mode to the layout
        var layout = {
            title: `Median Price Per Square Foot In ${year}`,
            margin: {
            l: 200,
            r: 100,
            t: 100,
            b: 100
            }
        };
        
        // Render the plot to the div tag with id "plot"
        Plotly.newPlot("bar", trace1, layout);




    });

}

function init(){
    //dropdown select year
    // Grab a reference to the dropdown select element
    var selector = d3.select("#selYear");

    // Use the list of sample names to populate the select options
    d3.json("/cities").then((citiesData) => {
        d3.json("/names").then((city)=>{
        //get square foot price for each city in that year
        var years= Object.keys(citiesData[city[0]]["Median Price Per Square Foot"]); 
        console.log("year",years);
        years.forEach((year) => {
        selector
            .append("option")
            .text(year)
            .property("value", year);
        });


    // Use the first sample from the list to build the initial plots
    const firstYear = years[0];
    barcity(firstYear);
    });
});

}

function optionChanged(newYear){
    // Fetch new year each time a new year is selected
    barcity(newYear);

}

init();