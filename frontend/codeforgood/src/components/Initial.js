import React from 'react'
import { Link } from "react-router-dom";

export default function Initial() {
  return (
    <div className="body1">
      <div className="bg">
        <img src={require('./school-kids.jpg')} alt="" />
      </div>

      <div className="welcome">
        <p>Welcome to Our Platform</p>
        <p>Link place where you learn the essentials</p>
      </div>

      <Link to="/student">
        <div className="student">
          <p>Are you Link Student?</p>
          <p>Click here</p>
        </div>
      </Link>

      <Link to="/volunteer">
        <div className="teacher">
          <p>Are you Link volunteer?</p>
          <p>Click here</p>
        </div>
      </Link>

      <Link to="/admin">
        <div className="admin">
          <p>Are you an Admin?</p>
          <p>Click here</p>
        </div>
      </Link>

      <div className="we-are">
        <div className="container">
          <p className="we-are-heading">We are</p>
          <button type="button" className="btn btn-primary we-are-schools">5 states</button>
          <button type="button" className="btn btn-primary we-are-schools">41+ Schools</button>
          <button type="button" className="btn btn-primary we-are-schools">20000+ students</button>
          <button type="button" className="btn btn-primary we-are-schools">100+ teachers</button>
        </div>
      </div>

      <div className="gallery-div">
        <p>Gallery</p>
        <div id="carouselExampleIndicators" className="carousel slide gallery" data-bs-ride="carousel">
          <div className="carousel-indicators">
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" className="active" aria-current="true" aria-label="Slide 1"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
          </div>
          <div className="carousel-inner">
            <div className="carousel-item active">
              <img src={require("./gallery1.jpg")} className="d-block w-100 gallery-images" alt="gallery images" />
            </div>
            <div className="carousel-item">
              <img src={require("./gallery2.jpg")} className="d-block w-100 gallery-images" alt="gallery images" />
            </div>
            <div className="carousel-item">
              <img src={require("./gallery3.jpg")} className="d-block w-100 gallery-images" alt="gallery images" />
            </div>
          </div>
          <button className="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
            <span className="carousel-control-prev-icon" aria-hidden="true"></span>
            <span className="visually-hidden">Previous</span>
          </button>
          <button className="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
            <span className="carousel-control-next-icon" aria-hidden="true"></span>
            <span className="visually-hidden">Next</span>
          </button>
        </div>
      </div>

      <div className="partners">
        <p>Partners</p>
        <div className="partners-img">
          <img src={require("./partner1.png")} alt="partners" />
        </div>
        <div className="partners-img">
          <img src={require("./partner2.png")} alt="partners" />
        </div>
        <div className="partners-img">
          <img src={require("./partner3.png")} alt="partners" />
        </div>
      </div>
      <div className="last"></div>

    </div>
  )
}
