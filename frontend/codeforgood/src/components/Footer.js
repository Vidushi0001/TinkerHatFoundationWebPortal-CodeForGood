import React from 'react'
import { Link } from "react-router-dom";
export default function Footer() {
  return (
    <div>
<footer className="page-footer font-small blue pt-4 bb">

  <div className="container-fluid text-center text-md-left">

    <div className="row">

      <div className="col-md-6 mt-md-0 mt-3">

        <h1 className="text-uppercase">10 on 10 </h1>
        <h3 class="bb3">Teaching the the present, Building the Future </h3>

      </div>

      <hr className="clearfix w-100 d-md-none pb-3"/>

      <div className="col-md-3 mb-md-0 mb-3">

        <h5 className="text-uppercase">Explore</h5>

        <ul className="list-unstyled">
          <li>
            <Link to="#!">Study Material</Link>
          </li>
          <li>
            <Link to="#!">Q and A</Link>
          </li>
          <li>
            <Link to="#!">Tests</Link>
          </li>
          <li>
            <Link to="#!">Diagnostic Analysis</Link>
          </li>
        </ul>

      </div>

      <div className="col-md-3 mb-md-0 mb-3">

        <h5 className="text-uppercase">Get Started</h5>

        <ul className="list-unstyled ">
          <li>
            <Link to="#!">Students</Link>
          </li>
          <li>
            <Link to="#!">Volunteers</Link>
          </li>
          <li>
            <Link to="#!">Admins</Link>
          </li>
   
        </ul>

      </div>

    </div>

  </div>

  <div className="footer-copyright text-center py-3">© 2022 Copyright &nbsp;&nbsp;:&nbsp;&nbsp; 
    <Link to="/"> 10on10.com</Link>
  </div>

</footer>
    </div>
  )
}
