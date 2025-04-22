import React from "react";

function ResultDisplay({ results }) {
	// Helper function to format sentiment data
	const formatSentiment = (sentimentData) => {
		if (!sentimentData) return null;

		const { sentiment, score, confidence } = sentimentData;

		return (
			<div className={`result-container ${sentiment}`}>
				<h3 style={{ textTransform: "capitalize" }}>{sentiment}</h3>
				<p>Score: {score.toFixed(2)}</p>
				<p>Confidence: {(confidence * 100).toFixed(1)}%</p>
			</div>
		);
	};

	return (
		<div className="card">
			<h2>Analysis Results</h2>

			<div style={{ display: "flex", flexWrap: "wrap", gap: "20px" }}>
				{results.text_sentiment && (
					<div style={{ flex: "1 1 300px" }}>
						<h3>Text Analysis</h3>
						{formatSentiment(results.text_sentiment)}
					</div>
				)}

				{results.image_sentiment && (
					<div style={{ flex: "1 1 300px" }}>
						<h3>Image Analysis</h3>
						{formatSentiment(results.image_sentiment)}
					</div>
				)}
			</div>

			{results.combined_sentiment && (
				<div style={{ marginTop: "20px" }}>
					<h3>Combined Analysis</h3>
					{formatSentiment(results.combined_sentiment)}
					<p>
						Text contribution:{" "}
						{results.combined_sentiment.text_contribution * 100}%<br />
						Image contribution:{" "}
						{results.combined_sentiment.image_contribution * 100}%
					</p>
				</div>
			)}
		</div>
	);
}

export default ResultDisplay;
