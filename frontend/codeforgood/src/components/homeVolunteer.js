import React from 'react'
import './homeVolunteer.css'

export default function homeVolunteer() {
    return (
        <div>
            <div className="classes container">
                <div className="classes-heading container mt-3">Live Classes Schedule</div>

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
                                        <div className="progress-bar bg-info" role="progressbar" style={{ width: '100%' }}
                                            aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">Physics : 10 AM</div>
                                    </div>
                                    <button type="button" className="btn btn-success btn-sm center">Start Class</button>
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
                                        <div className="progress-bar bg-info" role="progressbar" style={{ width: '100%' }}
                                            aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">Physics : 12 PM</div>
                                    </div>
                                    <button type="button" className="btn btn-success btn-sm center">Start Class</button>

                                    <div className="progress class-progress">
                                        <div className="progress-bar bg-info" role="progressbar" style={{ width: '100%' }}
                                            aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">Physics : 02 PM</div>
                                    </div>
                                    <button type="button" className="btn btn-success btn-sm center">Start Class</button>
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
                                        <div className="progress-bar bg-info" role="progressbar" style={{ width: '100%' }}
                                            aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">Physics : 06 PM</div>
                                    </div>
                                    <button type="button" className="btn btn-success btn-sm center">Start Class</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div className="report container">
                <div className="student-report">
                    <p>Total Students Joined</p>
                    <div className="report-progress progress">
                        <div className="progress-bar bg-success" role="progressbar" style={{ width: '75%' }} aria-valuenow="15"
                            aria-valuemin="0" aria-valuemax="100">755</div>
                    </div>
                </div>
            </div>

            <div className="notes container">
                <button type="button" className="btn btn-primary btn-lg notes-btn">
                    Videos <span className="badge bg-danger">4</span>
                </button>
                <button type="button" className="btn btn-primary btn-lg notes-btn">
                    PPTs <span className="badge bg-danger">8</span>
                </button>
                <button type="button" className="btn btn-primary btn-lg notes-btn">
                    PDFs <span className="badge bg-danger">1</span>
                </button>
                <button type="button" className="btn btn-primary btn-lg notes-btn">
                    Other References <span className="badge bg-danger"> 7</span>
                </button>
            </div>

        </div>
        
    )
}
