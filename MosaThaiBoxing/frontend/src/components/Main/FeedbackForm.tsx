import React, { useState } from 'react';
import '../../styles/MainPage.css';


interface FormData {
    name: string;
    email: string;
    phone_number: string;
    text: string;
}

const FeedbackForm: React.FC = () => {
    const [formData, setFormData] = useState<FormData>({
        name: '',
        email: '',
        phone_number: '',
        text: '',
    });

    const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
        const { name, value } = e.target;
        setFormData((prevData) => ({
            ...prevData,
            [name]: value,
        }));
    };

    return (
        <div className="main-page_form-container">
            <form className="main-page_form">
                <input
                        className="form_input"
                        type="text"
                        name="name"
                        placeholder="First and lastname"
                        value={formData.name}
                        onChange={handleChange}
                        required
                    />
                <br />
                <input
                        className="form_input"
                        type="email"
                        name="email"
                        placeholder="Email"
                        value={formData.email}
                        onChange={handleChange}
                        required
                    />
                <br />
                <input
                        className="form_input"
                        type="tel"
                        name="phone_number"
                        placeholder="Phone number"
                        value={formData.phone_number}
                        onChange={handleChange}
                        required
                    />
                <br />
                <input
                        className="form_input"
                        id="textarea"
                        name="text"
                        placeholder="Notice"
                        value={formData.text}
                        onChange={handleChange}
                        required
                    />
                <br />
                <button type="submit" id="feedback-btn">Send</button>
            </form>
        </div>
    );
};

export default FeedbackForm;
