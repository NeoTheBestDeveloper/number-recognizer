const LINE_WIDTH = 14;

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
		ctx.arc(x, y, LINE_WIDTH / 2, 0, Math.PI * 2);
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

const predict = () => {
	canvas.toBlob(async (blob) => {
		// Convert canvas img to file.
		const response = await predictAPI(blob);
		showAlert(response.num, "message");
	}, "image/png");
};
