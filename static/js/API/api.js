const predictAPI = async (numImage) => {
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
		showAlert("Ошибка" + response.status, "error");
	}
};
