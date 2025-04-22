import React, { useState } from "react";
import Header from "./components/Header";
import TextInput from "./components/TextInput";
import ImageUpload from "./components/ImageUpload";
import ResultDisplay from "./components/ResultDisplay";
import "./index.css";

function App() {
	const [text, setText] = useState("");
	const [image, setImage] = useState(null);
	const [results, setResults] = useState(null);
	const [loading, setLoading] = useState(false);
	const [error, setError] = useState("");

	const handleSubmit = async (e) => {
		e.preventDefault();

		if (!text && !image) {
			setError("Please enter text or upload an image");
			return;
		}

		setLoading(true);
		setError("");

		try {
			const formData = new FormData();
			if (text) formData.append("text", text);
			if (image) formData.append("image", image);

			const response = await fetch("http://localhost:8000/analyze", {
				method: "POST",
				body: formData,
			});

			if (!response.ok) {
				throw new Error("Failed to analyze sentiment");
			}

			const data = await response.json();
			setResults(data);
		} catch (err) {
			setError(err.message);
		} finally {
			setLoading(false);
		}
	};

	return (
		<div className="container">
			<Header />

			<div className="card">
				<h2>Analyze Sentiment</h2>
				<form onSubmit={handleSubmit}>
					<TextInput text={text} setText={setText} />
					<ImageUpload setImage={setImage} />

					{error && <p style={{ color: "red" }}>{error}</p>}

					<button type="submit" className="btn btn-primary" disabled={loading}>
						{loading ? "Analyzing..." : "Analyze Sentiment"}
					</button>
				</form>
			</div>

			{results && <ResultDisplay results={results} />}
		</div>
	);
}

export default App;
