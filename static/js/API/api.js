const predictAPI = async (numImage) => {
	// Send img file to api and getting preicted number.
	const formData = new FormData();
	formData.append("img", numImage);
	const response = await fetch("/predict", {
		method: "POST",
		body: formData,
	});
	if (response.ok) {
		const predict_num = await response.json();
		return predict_num;
	} else {
		showAlert("Ошибка " + response.status);
	}
};

const saveImageAPI = async (numImage, lineWidth, rightNumber) => {
	// Send img file and other metadata for saving it on server.
	const formData = new FormData();
	formData.append("img", numImage);
	formData.append("line_width", lineWidth);
	formData.append("right_number", rightNumber);
	const response = await fetch("/save-image", {
		method: "POST",
		body: formData,
	});

	if (!response.ok) {
		showAlert("Ошибка сохранения фото " + response.status);
	}
};
