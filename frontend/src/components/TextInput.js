import React from "react";

function TextInput({ text, setText }) {
	return (
		<div className="form-group">
			<label htmlFor="text">Text to analyze:</label>
			<textarea
				id="text"
				className="form-control"
				value={text}
				onChange={(e) => setText(e.target.value)}
				rows="4"
				placeholder="Enter text here..."
			></textarea>
		</div>
	);
}

export default TextInput;
