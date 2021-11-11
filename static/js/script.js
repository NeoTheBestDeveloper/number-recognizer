let LINE_WIDTH = 10;

// Init canvas field.
const canvas = document.querySelector(".draw-field");
const ctx = canvas.getContext("2d");

let isMouseDown = false;
ctx.lineWidth = LINE_WIDTH;

// Set event listeners for draw working. Painter must draw line only when mouse is down.
canvas.addEventListener("mousedown", () => {
	isMouseDown = true;
});

canvas.addEventListener("mouseup", () => {
	isMouseDown = false;
	ctx.beginPath();
});

canvas.onmousemove = (e) => {
	// Painter draw line when mouse move over field, function draw circle in point when mouse down.
	// Then function draw line, because we have gaps between circles.

	if (isMouseDown) {
		// Set circle position.
		const x = e.offsetX;
		const y = e.offsetY;

		// Draw line.
		ctx.lineTo(x, y);
		ctx.stroke();

		// Draw circle.
		ctx.beginPath();
		ctx.arc(x, y, Math.round(LINE_WIDTH / 2), 0, Math.PI * 2);
		ctx.fill();

		// Delete some artefacts.
		ctx.beginPath();
		ctx.moveTo(x, y);
	}
};

const showAlert = (message, type) => {
	const alert_div = document.querySelector("#alert");
	alert_div.innerText = message;
	alert_div.className = type;
};

const changeLineWidth = (range) => {
	// Change range state.
	const rangeState = document.querySelector(".line-width_state");
	rangeState.innerText = range.value;

	LINE_WIDTH = range.value;
	ctx.lineWidth = LINE_WIDTH;
};

const toggleDataCollectMode = (e) => {
	// Toggle switch button state.
	const switchBtn = document.querySelector(".switch-btn");
	switchBtn.classList.toggle("switch-on");

	// Toggle switch button text state.
	const switchBtnState = document.querySelector(".switch-button_state");
	if (switchBtnState.innerText == "Включен")
		switchBtnState.innerText = "Выключен";
	else switchBtnState.innerText = "Включен";

	// Toggle data collecting showing.
	const dataColllectingDiv = document.querySelector(
		".data-collection_content",
	);
	dataColllectingDiv.classList.toggle("hide");

	const sendImageBtn = document.querySelector(".send-image");
	sendImageBtn.classList.toggle("hide");

	const predictBtn = document.querySelector(".predict");
	predictBtn.classList.toggle("hide");
};

const predict = () => {
	canvas.toBlob(async (blob) => {
		// Clear canvas field.
		ctx.clearRect(0, 0, canvas.width, canvas.height);

		// Convert canvas img to file.
		const response = await predictAPI(blob);
		showAlert(response.num, "message");
	}, "image/png");
};

const saveImage = () => {
	canvas.toBlob(async (blob) => {
		// Clear canvas field.
		ctx.clearRect(0, 0, canvas.width, canvas.height);

		// Getting a right number.
		const rightNumber = document.querySelector("right-number");
		rightNumber = rightNumber.value;

		// Convert canvas img to file.
		const response = await saveImageAPI(blob, LINE_WIDTH, rightNumber);
		console.log(response);
	}, "image/png");
};

// Sinchronize range state text and range value.
changeLineWidth(document.querySelector("#line-width"));
