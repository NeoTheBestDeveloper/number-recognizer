const canvas = document.querySelector(".draw-field");
let alert_div = document.querySelector(".alert");
const ctx = canvas.getContext("2d");
let isMouseDown = false;
ctx.lineWidth = 14;

canvas.addEventListener("mousedown", () => {
	isMouseDown = true;
});

canvas.addEventListener("mouseup", () => {
	isMouseDown = false;
	ctx.beginPath();
});

canvas.onmousemove = (e) => {
	if (isMouseDown) {
		const x = e.offsetX;
		const y = e.offsetY;

		ctx.lineTo(x, y);
		ctx.stroke();

		ctx.beginPath();
		ctx.arc(x, y, 7, 0, Math.PI * 2);
		ctx.fill();

		ctx.beginPath();
		ctx.moveTo(x, y);
	}
};

const showAlert = (message, type) => {
	alert_div.innerText = message;
	alert_div.className = type;
};

const predict = (e) => {
	let response;
	canvas.toBlob(async (blob) => {
		response = await predictAPI(blob);
		showAlert(response.num, "message");
	}, "image/png");
};
