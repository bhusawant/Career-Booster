import React, { useState } from 'react';
import axios from 'axios';
import "../styles/chatbot.css"

function App() {
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');

  const askQuestion = async () => {
    try {
      console.log(question)
      const res = await axios.post('http://localhost:5000/ask', { question });
      setAnswer(res.data.answer);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="App">
      <h1>Chatbot</h1>
      <input
        type="text"
        placeholder="Ask a question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />
      <button onClick={askQuestion}>Ask</button>
      {answer && (
        <div className="response">
          <strong>Response:</strong>
          <p>{answer}</p>
        </div>
      )}
    </div>
  );
}

export default App;