import React, { useEffect, useState } from 'react';

const App: React.FC = () => {
    const [lessons, setLessons] = useState([]);

    useEffect(() => {
        fetchLessons();
    }, []);

    const fetchLessons = async () => {
        try {
            const response = await fetch('http://localhost:8000/lessons/');
            const data = await response.json();
            setLessons(data);
            console.log(data);
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <div>
            {lessons.map((lesson: any) => (
                <div key={lesson.id}>
                    <h2>{lesson.title}</h2>
                    {lesson.questions.map((question: any) => (
                        <div key={question.id}>
                            <h4>{question.text}</h4>
                            <ul>
                                {question.answers.map((answer: any) => (
                                    <li key={answer.id}>{answer.text}</li>
                                ))}
                            </ul>
                        </div>
                    ))}
                </div>
            ))}
        </div>
    );
};

export default App;
