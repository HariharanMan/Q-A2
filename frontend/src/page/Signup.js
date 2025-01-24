
import React, { useState, useEffect } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import axios from 'axios';
import Heroimg from "../assets/login-hero-img.png"

function SignUpPage() {
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [email, setEmail] = useState('');
  const [phone, setPhone] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [error, setError] = useState('');
  const [privacyChecked, setPrivacyChecked] = useState(false);
  const [fieldErrors, setFieldErrors] = useState({});
  const [isEmailVerification, setIsEmailVerification] = useState(false);
  const [isPhoneVerification, setIsPhoneVerification] = useState(false);
  const [emailOtp, setEmailOtp] = useState('');
  const [phoneOtp, setPhoneOtp] = useState('');

  // New state variables for timers and expiration
  const [emailTimer, setEmailTimer] = useState(300); // 5 minutes in seconds
  const [phoneTimer, setPhoneTimer] = useState(300);
  const [emailOtpExpired, setEmailOtpExpired] = useState(false);
  const [phoneOtpExpired, setPhoneOtpExpired] = useState(false);
  const [phoneError, setPhoneError] = useState('');
  const [showPassword, setShowPassword] = useState(false); // State for toggling password visibility
  const [emailOtpAttempts, setEmailOtpAttempts] = useState(0); // Track email OTP attempts
  const [phoneOtpAttempts, setPhoneOtpAttempts] = useState(0); // Track phone OTP attempts

  const navigate = useNavigate();

  // Timer effect for email OTP
  useEffect(() => {
    let interval;
    if (isEmailVerification && emailTimer > 0) {
      interval = setInterval(() => {
        setEmailTimer((prev) => {
          if (prev <= 1) {
            setEmailOtpExpired(true);
            clearInterval(interval);
            return 0;
          }
          return prev - 1;
        });
      }, 1000);
    }
    return () => clearInterval(interval);
  }, [isEmailVerification, emailTimer]);

  // Timer effect for phone OTP
  useEffect(() => {
    let interval;
    if (isPhoneVerification && phoneTimer > 0) {
      interval = setInterval(() => {
        setPhoneTimer((prev) => {
          if (prev <= 1) {
            setPhoneOtpExpired(true);
            clearInterval(interval);
            return 0;
          }
          return prev - 1;
        });
      }, 1000);
    }
    return () => clearInterval(interval);
  }, [isPhoneVerification, phoneTimer]);

  const formatTime = (seconds) => {
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = seconds % 60;
    return `${minutes}:${remainingSeconds.toString().padStart(2, '0')}`;
  };

  const validatePassword = (password) => {
    const passwordRegex = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{3,}$/;
    return passwordRegex.test(password);
  };

  const validateAndSetPhone = (value) => {
    const phoneRegex = /^\d*$/;
    if (!phoneRegex.test(value)) {
      setPhoneError('Please enter numbers only');
      return;
    }
    if (value.length > 10) {
      setPhoneError('Phone number cannot exceed 10 digits');
      return;
    }
    setPhoneError('');
    setPhone(value);
    if (value.length === 10) {
      setPhoneError('');
    } else if (value.length > 0) {
      setPhoneError('Phone number must be 10 digits');
    }
  };

  const handleEmailVerification = async () => {
    if (!email) {
      setError('Please enter a valid email address.');
      return;
    }
    try {
      setError('');
      setIsEmailVerification(true);
      setEmailTimer(300);
      setEmailOtpExpired(false);
      setEmailOtpAttempts(0); // Reset attempts on new OTP request
      await axios.post('http://127.0.0.1:8000/api/request-email-otp/', { email });
    } catch (error) {
      setError('Failed to request email verification. Please try again.');
    }
  };

  const handlePhoneVerification = async () => {
    if (!phone || phone.length !== 10) {
      setError('Please enter a valid 10-digit phone number.');
      return;
    }
    try {
      setError('');
      setIsPhoneVerification(true);
      setPhoneTimer(300);
      setPhoneOtpExpired(false);
      setPhoneOtpAttempts(0); // Reset attempts on new OTP request
      await axios.post('http://127.0.0.1:8000/api/request-phone-otp/', { phone });
    } catch (error) {
      setError('Failed to request phone verification. Please try again.');
    }
  };

  const handleEmailOtpSubmission = async () => {
    if (emailOtpExpired) {
      setError('OTP has expired. Please request a new one.');
      return;
    }
    if (emailOtpAttempts >= 3) {
      setError('Too many incorrect attempts. Please request a new OTP.');
      return;
    }
    try {
      setError('');
      await axios.post('http://127.0.0.1:8000/api/verify-email-otp/', { email, otp: emailOtp });
      alert('Email verified successfully!');
      setIsEmailVerification(false);
    } catch (error) {
      setError('Invalid OTP. Please try again.');
      setEmailOtpAttempts((prev) => prev + 1); // Increment OTP attempts
    }
  };

  const handlePhoneOtpSubmission = async () => {
    if (phoneOtpExpired) {
      setError('OTP has expired. Please request a new one.');
      return;
    }
    if (phoneOtpAttempts >= 3) {
      setError('Too many incorrect attempts. Please request a new OTP.');
      return;
    }
    try {
      setError('');
      await axios.post('http://127.0.0.1:8000/api/verify-phone-otp/', { phone, otp: phoneOtp });
      alert('Phone verified successfully!');
      setIsPhoneVerification(false);
    } catch (error) {
      setError('Invalid OTP. Please try again.');
      setPhoneOtpAttempts((prev) => prev + 1); // Increment OTP attempts
    }
  };

  const handleSignUp = async () => {
    if (!firstName || !lastName || !email || !phone || !password || !confirmPassword || !privacyChecked) {
      setError('Please fill all the required fields and agree to the privacy terms.');
      return;
    }
    if (password !== confirmPassword) {
      setError('Passwords do not match.');
      return;
    }
    if (!validatePassword(password)) {
      setError('Password must be at least 3 characters long, contain letters, numbers, and at least one symbol.');
      return;
    }
    if (phone.length !== 10) {
      setError('Please enter a valid 10-digit phone number.');
      return;
    }
    setError('');

    const userData = {
      firstName,
      lastName,
      email,
      phone,
      password,
      confirmPassword
    };

    try {
      const response = await axios.post('http://127.0.0.1:8000/api/signup/', userData);
      if (response.status === 200 || response.status === 201) {
        alert('Sign-up successful! Welcome to our platform!');
        navigate('/login');
      }
    } catch (error) {
      console.error('Error during sign-up:', error);
      setError('An error occurred during sign-up. Please try again.');
    }
  };

  const handleBack = () => {
    navigate('/login');
  };

  return (
    <div className="flex min-h-screen bg-white">
        <div className="hidden md:flex flex-col justify-center items-center w-1/3 bg-[#3c7a89] text-white p-10 m-10 rounded-lg">
              <img src={Heroimg}/>
               
            </div>
      <div className="w-1/2 flex flex-col items-center justify-center p-6">
        <h1 className="text-4xl text-gray-800 mb-8">Sign Up</h1>
        {error && <p className="text-red-500 text-sm mb-4">{error}</p>}
        
        <div className="w-full max-w-md space-y-4">
          <input
            type="text"
            placeholder="First Name (Required)"
            value={firstName}
            onChange={(e) => setFirstName(e.target.value)}
            className="w-full p-3 border border-gray-300 rounded-md shadow-sm text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
          />
          <input
            type="text"
            placeholder="Last Name (Required)"
            value={lastName}
            onChange={(e) => setLastName(e.target.value)}
            className="w-full p-3 border border-gray-300 rounded-md shadow-sm text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
          />
          <input
            type="email"
            placeholder="Email Address (Required)"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="w-full p-3 border border-gray-300 rounded-md shadow-sm text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
          />
          <button
            onClick={handleEmailVerification}
            className="w-full p-3 bg-[#3c7a89] text-white py-2 px-4 rounded-md shadow-md hover:bg-blue-600 focus:outline-none focus:ring-4 focus:ring-blue-300 font-medium transition-all mt-2"
            disabled={isEmailVerification}
          >
            {isEmailVerification ? `Resend Email OTP in ${formatTime(emailTimer)}` : 'Verify Email'}
          </button>
          <input
            type="text"
            placeholder="Enter OTP"
            value={emailOtp}
            onChange={(e) => setEmailOtp(e.target.value)}
            className="w-full p-3 border border-gray-300 rounded-md shadow-sm text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 mt-2"
          />
          <button
            onClick={handleEmailOtpSubmission}
            className="w-full p-3 bg-[#3c7a89] text-white py-2 px-4 rounded-md shadow-md hover:bg-blue-600 focus:outline-none focus:ring-4 focus:ring-blue-300 font-medium transition-all mt-2"
          >
            Submit OTP
          </button>
          <input
            type="text"
            placeholder="Phone Number (Required)"
            value={phone}
            onChange={(e) => validateAndSetPhone(e.target.value)}
            className="w-full p-3 border border-gray-300 rounded-md shadow-sm text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 mt-2"
          />
          {phoneError && <p className="text-red-500 text-sm mt-2">{phoneError}</p>}
          <button
            onClick={handlePhoneVerification}
            className="w-full p-3 bg-[#3c7a89] text-white py-2 px-4 rounded-md shadow-md hover:bg-blue-600 focus:outline-none focus:ring-4 focus:ring-blue-300 font-medium transition-all"
            disabled={isPhoneVerification}
          >
            {isPhoneVerification ? `Resend Phone OTP in ${formatTime(phoneTimer)}` : 'Verify Phone'}
          </button>
          <input
            type="text"
            placeholder="Enter OTP"
            value={phoneOtp}
            onChange={(e) => setPhoneOtp(e.target.value)}
            className="w-full p-3 border border-gray-300 rounded-md shadow-sm text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 mt-2"
          />
          <button
            onClick={handlePhoneOtpSubmission}
            className="w-full p-3 bg-[#3c7a89] text-white py-2 px-4 rounded-md shadow-md hover:bg-blue-600 focus:outline-none focus:ring-4 focus:ring-blue-300 font-medium transition-all mt-2"
          >
            Submit OTP
          </button>
          <input
            type={showPassword ? 'text' : 'password'}
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="w-full p-3 border border-gray-300 rounded-md shadow-sm text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 mt-2"
          />
          
          <input
            type={showPassword ? 'text' : 'password'}
            placeholder="Confirm Password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            className="w-full p-3 border border-gray-300 rounded-md shadow-sm text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 mt-2"
          />
          <button
            onClick={() => setShowPassword(!showPassword)}
            className="bg-[#3c7a89] text-white py-2 px-4 rounded-md shadow-md hover:bg-blue-600 focus:outline-none focus:ring-4 focus:ring-blue-300 font-medium transition-all mt-1"
          >
            {showPassword ? 'Hide Password' : 'Show Password'}
          </button>
          <div className="flex items-center mt-2">
            <input
              type="checkbox"
              checked={privacyChecked}
              onChange={(e) => setPrivacyChecked(e.target.checked)}
              className="text-orange-500"
            />
            <label className="text-black text-sm ml-2">I agree to the terms and conditions <p className='text-blue-400 underline cursor-pointer'onClick={() => window.location.href = "/privacy-policy"} >Read terms and conditions </p></label> 
          </div>
          <button
            onClick={handleSignUp}
            className="w-full p-3 bg-[#3c7a89] text-white py-2 px-4 rounded-md shadow-md hover:bg-blue-600 focus:outline-none focus:ring-4 focus:ring-blue-300 font-medium transition-all mt-4"
          >
            Sign Up
          </button>
          <div className="text-white mt-4">
            <span>Already have an account? </span>
            <Link to="/login" className="text-lg text-[#3c7a89]">Login</Link>
          </div>
        </div>
      </div>
    </div>
  );
}

export default SignUpPage;
