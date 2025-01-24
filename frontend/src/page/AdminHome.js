import React, { useState } from 'react';

const AdminHome = () => {
    const [questions, setQuestions] = useState([
        // Sample data, replace with actual data
        { id: 1, title: "What is Python?", author: "Hari", answers: "Python is a versatile, high-level programming language.", comments: 10 },
        { id: 2, title: "How to manage memory in Python?", author: "Mem2", answers: "Python uses garbage collection and reference counting.", comments: 8 },
        // Add more questions as needed
    ]);

    const toggleAnswer = (id) => {
        const updatedQuestions = questions.map(question => {
            if (question.id === id) {
                question.showAnswer = !question.showAnswer;
            }
            return question;
        });
        setQuestions(updatedQuestions);
    };

    return (
        <div style={styles.container}>
            <h1>Admin Page</h1>
            <div style={styles.listGroup}>
                {questions.map((question, index) => (
                    <div key={question.id} style={styles.listGroupItem}>
                        <h5>{question.title}</h5>
                        <p><strong>Author:</strong> {question.author}</p>
                        <p><strong>Comments:</strong> {question.comments}</p>
                        <button onClick={() => toggleAnswer(question.id)} style={styles.button}>Toggle Answer</button>
                        {question.showAnswer && <p>{question.answers}</p>}
                    </div>
                ))}
            </div>
        </div>
    );
};

const styles = {
    container: {
        padding: '20px',
        fontFamily: 'Arial, sans-serif'
    },
    listGroup: {
        marginTop: '20px'
    },
    listGroupItem: {
        border: '1px solid #ddd',
        borderRadius: '4px',
        padding: '10px',
        marginBottom: '10px'
    },
    button: {
        backgroundColor: '#007bff',
        color: 'white',
        border: 'none',
        padding: '10px 20px',
        borderRadius: '4px',
        cursor: 'pointer'
    }
};

export default AdminHome;