import "./App.css";
import LoginAdmin from "./components/loginAdmin.js";
import LoginVolunteer from "./components/loginVolunteer.js";
import LoginStudent from "./components/loginStudent.js";
import SignUpStudent from "./components/signupStudent.js";
import SignUpVolunteer from "./components/signupVolunteer.js";
import Footer from './components/Footer.js';
import Initial from './components/Initial.js';
import Student from "./components/student.js";
import Volunteer from "./components/volunteer.js";
import Admin from "./components/admin.js";
import Studymaterial from "./components/studymaterial.js";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import React from 'react'
import { useState ,useEffect} from "react";

function App() {
  const [signedIn, setsignedIn] = useState(false)
  useEffect(() => {
   
  }, [signedIn])
  
  return (
    <Router>
      <div className="Container">
        <Routes>
        <Route exact path="/" element = {<Initial />} >
          </Route>
          <Route exact path="/student" element={<Student student={"student"}/>}>   
          </Route>
          <Route exact path="/volunteer" element={<Volunteer/>}>            
          </Route>
          <Route exact path="/admin" element={<Admin/>}>            
          </Route>
          <Route exact path="/loginStudent" element={<LoginStudent/>}>            
          </Route>
          <Route exact path="/studyMaterial" element={<Studymaterial/>}>            
          </Route>
          <Route exact path="/teacher" element={<LoginVolunteer/>}>            
          </Route>
          <Route exact path="/loginAdmin" element={<LoginAdmin/>}>            
          </Route>
          <Route exact path="/signUpStudent" element={<SignUpStudent/>}>            
          </Route>
          <Route exact path="/signUpVolunteer" element={<SignUpVolunteer/>}>            
          </Route>
        </Routes>
        <Footer/>
      </div>
    </Router>
  );
}

export default App;
