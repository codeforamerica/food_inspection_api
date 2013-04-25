

$(function(){

  var map;
  var markers = [];
  var loadData = function(e){
    console.log("map move:", e);
    
    var bounds = map.getBounds();
    console.log("map bounds:", bounds)

    var nw = bounds.getNorthWest().lat+","+bounds.getNorthWest().lng;
    var se = bounds.getSouthEast().lat+","+bounds.getSouthEast().lng;


    $.ajax("http://localhost:5000/foodInspection/v1/businesses.json", 
           {data:{nw:nw, se:se, page_size:"10000"},
            dataType:"json",
            success:function(data){
              console.log("got data:",data);
              
              for(m in markers){
                map.removeLayer(markers[m]);
              }
              for(r in data.results){
                var biz = data.results[r];
                markers.push(L.marker([biz.location.lat, biz.location.lon],
                                     {title:biz.name,
                                     riseOnHover:true}).addTo(map));
              }

            }});

  }

  

  wax.tilejson('http://api.tiles.mapbox.com/v2/dmt.map-f9qb0tnz.jsonp',
               function(tilejson) {
                 map = new L.Map('map')
                 map.on('load', loadData);
                 map.addLayer(new wax.leaf.connector(tilejson))
                   .setView(new L.LatLng(37.7756,-122.4402), 15);

                 map.on('moveend', loadData);


               });



});

