import React from 'react'
import NavbarStudent from "./navbarStudent.js";
import HomeStudent from "./homeStudent.js";
export default function student(props) {
  return (
    <div>
        <NavbarStudent/>
        <p>{props.student}</p>
        <HomeStudent/>
    </div>
  )
}
