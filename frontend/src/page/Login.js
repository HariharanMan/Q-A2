import React, { useState } from 'react';

const Login = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [message, setMessage] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();

        const response = await fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({ email, password })
        });

        const data = await response.json();
        if (data.error) {
            setMessage(<div style={styles.alertDanger}>{data.error}</div>);
        } else {
            setMessage(<div style={styles.alertSuccess}>{data.message}</div>);
        }
    };

    const getCookie = (name) => {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    };

    return (
        <div style={styles.container}>
            <h1 style={styles.title}>Login</h1>
            <form id="loginForm" onSubmit={handleSubmit} style={styles.form}>
                <div style={styles.formGroup}>
                    <label htmlFor="email">Email:</label>
                    <input
                        type="email"
                        id="email"
                        name="email"
                        placeholder="Enter your email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                        style={styles.input}
                    />
                </div>
                <div style={styles.formGroup}>
                    <label htmlFor="password">Password:</label>
                    <input
                        type="password"
                        id="password"
                        name="password"
                        placeholder="Enter your password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                        style={styles.input}
                    />
                </div>
                <button type="submit" style={styles.button}>Login</button>
            </form>
            <div id="message">{message}</div>
        </div>
    );
};

const styles = {
    container: {
        marginTop: '50px',
        padding: '20px',
        fontFamily: 'Arial, sans-serif',
        maxWidth: '400px',
        margin: '0 auto',
        border: '1px solid #ddd',
        borderRadius: '4px'
    },
    title: {
        textAlign: 'center',
        marginBottom: '20px'
    },
    form: {
        display: 'flex',
        flexDirection: 'column'
    },
    formGroup: {
        marginBottom: '15px'
    },
    input: {
        width: '100%',
        padding: '10px',
        borderRadius: '4px',
        border: '1px solid #ddd'
    },
    button: {
        backgroundColor: '#007bff',
        color: 'white',
        border: 'none',
        padding: '10px 20px',
        borderRadius: '4px',
        cursor: 'pointer'
    },
    alertDanger: {
        color: 'red',
        marginTop: '10px'
    },
    alertSuccess: {
        color: 'green',
        marginTop: '10px'
    }
};

export default Login;