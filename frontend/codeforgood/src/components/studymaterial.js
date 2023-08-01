import React, { useState } from "react";
import "../css/study_material.css";
import axios from "axios";
import { useEffect } from "react";
export default function Studymaterial() {
const fetchData=()=>{
    axios.get("http://127.0.0.1:8000/courses/api/").then(
        (response)=>{
            setState1(response.data)
        }
    )
}
    const [State1, setState1] = useState([])
    
    // obj=
useEffect(() => {
    fetchData();
}, [])

return (
      <div>
        <h1>Study Material</h1>
        <div class="main"></div>
        {State1.map((e)=>{
       return (
    
        <div class="card">       
          <div class="title">
            <h1>{e.course_name}</h1>
          </div>
          <div class="des">
           <a href={e.course_videos_link}> <button>Open</button></a>
          </div>
        </div>
             );})}

      </div>
    );


}
