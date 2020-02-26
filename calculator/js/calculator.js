/* jshint esversion: 6 */
/* jshint node: true */
/* jshint browser: true */
/* jshint jquery: true */
'use strict';

window.onload = function() {
	// Holds all of the display and calculation result
	var input = document.getElementById("inputBox");
	var container = document.getElementById("container");

	//Call Button Clickers
	container.addEventListener("click", function(e){
		buttonClick(e.target.id);
	});

	// Calculating numbers 
	var calc = document.getElementById("buttonEq");
	calc.addEventListener("click", calculate);

	
	//Creating a variable for clear method
	var c = document.getElementById("buttonc");
	c.addEventListener("click", erase);

	//Creates an input to calculate except (=), (c) buttons
	function buttonClick(buttonId) {
		if((buttonId != "buttonc") && (buttonId != "buttonEq")){
			var button = document.getElementById(buttonId);
			var tmp = buttonId;
			tmp = tmp.replace("button", "");
			entries(tmp);
		}
	}
	// Concatenating numbers
	function entries(tmp) {
		input.value += tmp;
	}

	function calculate() {
		if (input.value == ".") {
			alert("Enter Mathematical Expression: ")
			return;
		}
		input.value = eval(input.value);
	}

	function erase() {
		input.value = "";
	}
};





