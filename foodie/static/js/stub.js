function initMap() {
  var map = new google.maps.Map(document.getElementById('map'), 
  {
    zoom: 11,
    center: {lat: 41.876, lng: -87.624}
  });

  var kmlLayer = new google.maps.KmlLayer({
    url: 'http://data.vancouver.ca/download/kml/street_food_vendors.kmz',
    map: map
  });
}