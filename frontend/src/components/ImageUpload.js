import React, { useState } from "react";

function ImageUpload({ setImage }) {
	const [preview, setPreview] = useState("");

	const handleImageChange = (e) => {
		const file = e.target.files[0];
		if (file) {
			setImage(file);

			// Create preview URL
			const reader = new FileReader();
			reader.onload = () => {
				setPreview(reader.result);
			};
			reader.readAsDataURL(file);
		}
	};

	return (
		<div className="form-group">
			<label htmlFor="image">Image to analyze:</label>
			<input
				type="file"
				id="image"
				className="form-control"
				accept="image/*"
				onChange={handleImageChange}
			/>

			{preview && (
				<div style={{ marginTop: "10px" }}>
					<img
						src={preview}
						alt="Preview"
						style={{
							maxWidth: "100%",
							maxHeight: "200px",
							borderRadius: "4px",
						}}
					/>
				</div>
			)}
		</div>
	);
}

export default ImageUpload;
