//function to build bar chart that show price per square foot for each city
function barcity(city){
    url='/cities';
    d3.json(url).then(function(data){
        var avg_sale=[]
        var years=[]
        //get avg sale in that city
        years=(Object.keys(data[city]["Mean Sales Per Year"]));
        for (i in data[city]['Mean Sales Per Year']){
            avg_sale.push(data[city]['Mean Sales Per Year'][i]);  
        } 
        console.log("price",avg_sale);
        console.log("city",years);
        // Trace1 for the price per sq ft data
        var trace1 = [{
            x: years,
            y: avg_sale,
            type: 'line'
        }];
        
        var layout2 = {
            title: `Average Sales Per Year in ${city}`,
            margin: {
                l: 100,
                r: 100,
                t: 100,
                b: 100
                }
            };
            Plotly.newPlot('line', trace1, layout2);
    });

}

function init(){
    //dropdown select year
    // Grab a reference to the dropdown select element
    var selector2 = d3.select("#selcity");

    // Use the list of sample names to populate the select options
        d3.json("/names").then((cities)=>{
        cities.forEach((city) => {
        selector2
            .append("option")
            .text(city)
            .property("value", city);
        });


    // Use the first sample from the list to build the initial plots
    const firstcity = cities[0];
    barcity(firstcity);
    });
}

function optionChanged(newcity){
    // Fetch new year each time a new year is selected
    barcity(newcity);

}

init();