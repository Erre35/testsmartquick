$( document ).ready(function() {
    sendReq()
});

var getData =function () {

	var Placa = document.getElementById("Placa").value.toUpperCase()
	var Hora1 = document.getElementById("party1").value
	var Hora2 = document.getElementById("party2").value
	var Origen = document.getElementById("Origen").value
	var Destino = document.getElementById("Destino").value

	var formData = new FormData();

	formData.append("placa", Placa.toUpperCase());
	formData.append("hora_salida", Hora1);
	formData.append("hora_llegada", Hora2);
	formData.append("origen", Origen);
	formData.append("llegada", Destino);
	formData.append("actual_a", Origen);

	var xhr = new XMLHttpRequest();
	xhr.onload = function() {
		var myObject = JSON.parse(this.responseText);
		console.log("myObject post", myObject)
		location.reload();
	}
	xhr.open("POST", "http://127.0.0.1:8000/api/buses/");
	// xhr.setRequestHeader('Content-Type', 'application/form-data');
	xhr.send(formData);
	}



function sendReq() {
	const xhttp = new XMLHttpRequest();
	xhttp.onload = function() {
	var myObject = JSON.parse(this.responseText);
	console.log(myObject)
	var mymap = L.map('mapa').setView([4.612639, -74.0705], 8);

	L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 18,
		attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
			'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
		id: 'mapbox/streets-v11',
		tileSize: 512,
		zoomOffset: -1
	}).addTo(mymap);

	for (var i = 0; i < myObject.length; i++) {
		if(myObject[i].buses.length){
			var buses= "";
			for (var j = 0; j < myObject[i].buses.length; j++) {
				buses = buses + "<li>" + myObject[i].buses[j].placa + "</li>Hora salida: " + myObject[i].buses[j].hora_salida + "</br>Hora llegada:" + myObject[i].buses[j].hora_llegada 
			}
			L.marker([myObject[i].latitud, myObject[i].longitud]).addTo(mymap).bindPopup("<b><h6>" + myObject[i].name + "</b></h6><b>Capacidad:</b> " + myObject[i].capacidad + "<br /><b>Horario:</b> 6AM - 8PM <br /><b>Buses:</b> " + buses + "").openPopup();
		} else{
			L.marker([myObject[i].latitud, myObject[i].longitud]).addTo(mymap).bindPopup("<b><h6>" + myObject[i].name + "</b></h6><b>Capacidad:</b> " + myObject[i].capacidad + "<br /><b>Horario:</b> 6AM - 8PM <br /><b>Buses:</b> No hay buses actualmente").openPopup();
		}
	}

	}
	xhttp.open("GET", "http://127.0.0.1:8000/API/updateBusState");
	xhttp.send();
  }