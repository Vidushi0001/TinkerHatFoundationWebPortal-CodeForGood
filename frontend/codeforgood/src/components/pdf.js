import React from 'react'
import './1.css'
import {Link} from '.'
export default function pdf() {
  return (
    <div>

<h1>Science</h1>
    <h2>PDFs</h2>
    <div className="download-item">
        <i className="bi bi-file-earmark-pdf-fill my-pdfs"></i><br/>
        <Link to="./pdf_1.pdf" download>Electromagnetic Induction</Link><br/>
        
    </div>
    <div className="download-item">
        <i className="bi bi-file-earmark-pdf-fill my-pdfs"></i><br/>
        <Link to="./pdf_2.pdf" download>Air Around Us</Link>
    </div>
    <div className="download-item">
        <i className="bi bi-file-earmark-pdf-fill my-pdfs"></i><br/>
        <Link to="./pdf_1.pdf" download>Magnetism</Link>
    </div>
    <div className="download-item">
        <i className="bi bi-file-earmark-pdf-fill my-pdfs"></i><br />
        <Link to="./pdf_2.pdf" download>Inductors</Link>
    </div>
    <div className="download-item">
        <i className="bi bi-file-earmark-pdf-fill my-pdfs"></i><br />
        <Link to="./pdf_1.pdf" download>Organic Chemistry</Link>
    </div>
    <div className="download-item">
        <i className="bi bi-file-earmark-pdf-fill my-pdfs"></i><br />
        <Link to="./pdf_2.pdf" download>Inorganic Chemistry</Link>
    </div>
    </div>
  )
}
