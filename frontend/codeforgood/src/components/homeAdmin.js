import React from 'react'
import './homeAdmin.css'

export default function homeAdmin() {
  return (
    <>
<div className="classes container">
    <div className="classes-heading container mt-3 center">Live Classes Schedule</div>

    <div className="classes-schedule container mt-3">
        <div className="accordion" id="accordionExample">
            <div className="accordion-item">
                <h2 className="accordion-header" id="headingOne">
                    <button className="accordion-button" type="button" data-bs-toggle="collapse"
                        data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                        9 AM - 12 PM
                    </button>
                </h2>
                <div id="collapseOne" className="accordion-collapse collapse show" aria-labelledby="headingOne"
                    data-bs-parent="#accordionExample">
                    <div className="accordion-body">
                        <div className="progress class-progress">
                            <div className="progress-bar bg-success" role="progressbar" style={{width: '25%'}}
                                aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">English</div>
                        </div>
                        <div className="progress class-progress">
                            <div className="progress-bar bg-info" role="progressbar" style={{width: '50%'}}
                                aria-valuenow="50" aria-valuemin="0" aria-valuemax="100">Elementary Physics</div>
                        </div>
                        <div className="progress class-progress">
                            <div className="progress-bar bg-warning" role="progressbar" style={{width: '75%'}}
                                aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">Chemistry</div>
                        </div>
                        <div className="progress class-progress">
                            <div className="progress-bar bg-danger" role="progressbar" style={{width: '100%'}}
                                aria-valuenow="100" aria-valuemin="0" aria-valuemax="100">Data Structure</div>
                        </div>
                    </div>
                </div>
            </div>
            <div className="accordion-item">
                <h2 className="accordion-header" id="headingTwo">
                    <button className="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                        data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                        12 PM - 3 PM
                    </button>
                </h2>
                <div id="collapseTwo" className="accordion-collapse collapse" aria-labelledby="headingTwo"
                    data-bs-parent="#accordionExample">
                    <div className="accordion-body">
                        <div className="progress class-progress">
                            <div className="progress-bar bg-secondary" role="progressbar" style={{width: '25%'}}
                                aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">English</div>
                        </div>
                        <div className="progress class-progress">
                            <div className="progress-bar bg-secondary" role="progressbar" style={{width: '50%'}}
                                aria-valuenow="50" aria-valuemin="0" aria-valuemax="100">Elementary Physics</div>
                        </div>
                        <div className="progress class-progress">
                            <div className="progress-bar bg-secondary" role="progressbar" style={{width: '75%'}}
                                aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">Chemistry</div>
                        </div>
                        <div className="progress class-progress">
                            <div className="progress-bar bg-secondary" role="progressbar" style={{width: '100%'}}
                                aria-valuenow="100" aria-valuemin="0" aria-valuemax="100">Data Structure</div>
                        </div>
                    </div>
                </div>
            </div>
            <div className="accordion-item">
                <h2 className="accordion-header" id="headingThree">
                    <button className="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                        data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
                        3 PM - 6 PM
                    </button>
                </h2>
                <div id="collapseThree" className="accordion-collapse collapse" aria-labelledby="headingThree"
                    data-bs-parent="#accordionExample">
                    <div className="accordion-body">
                        <div className="progress class-progress">
                            <div className="progress-bar bg-secondary" role="progressbar" style={{width: '25%'}}
                                aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">English</div>
                        </div>
                        <div className="progress class-progress">
                            <div className="progress-bar bg-secondary" role="progressbar" style= {{width: '50%'}}
                                aria-valuenow="50" aria-valuemin="0" aria-valuemax="100">Elementary Physics</div>
                        </div>
                        <div className="progress class-progress">
                            <div className="progress-bar bg-secondary" role="progressbar" style={{width: '75%'}}
                                aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">Chemistry</div>
                        </div>
                        <div className="progress class-progress">
                            <div className="progress-bar bg-secondary" role="progressbar" style= {{width: '100%'}}
                                aria-valuenow="100" aria-valuemin="0" aria-valuemax="100">Data Structure</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
<div className="report container">
    <div className="student-report">
        <p>Student Report</p>
        <div className="report-progress progress">
            <div className="progress-bar bg-danger" role="progressbar" style={{width: '15%'}} aria-valuenow="15"
                aria-valuemin="0" aria-valuemax="100">15%</div>
            <div className="progress-bar bg-success" role="progressbar" style={{width: '50%'}} aria-valuenow="30"
                aria-valuemin="0" aria-valuemax="100">50%</div>
            <div className="progress-bar bg-info" role="progressbar" style={{width: '20%'}} aria-valuenow="20"
                aria-valuemin="0" aria-valuemax="100">20%</div>
        </div>
    </div>
</div>

<div className="notes container">
    <button type="button" className="btn btn-primary notes-btn">
        Add Notes and references
    </button>
    <button type="button" className="btn btn-primary notes-btn">
        Checkout various schools
    </button>
    <button type="button" className="btn btn-primary notes-btn">
        checkout student activity
    </button>
</div>
</>

  )
}
