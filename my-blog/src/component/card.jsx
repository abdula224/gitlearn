import React from 'react'
export default function Card(){
    return(
        <div>
           
        <div className="card " style={{width: "20rem"}} >
            <img src="/" alt="Not" className="card-img-top" />
            <div className="card-body">
                <h4 className="card-title">My News</h4>
                <p className="card-text ">TajaKhabar</p>
            </div>
            <a href='/' className="btn  btn-sm btn-primary">Go Anywhere</a>
        </div>
    
      {/* <div className="container my-4">
          <table className="table table-stripped table-hover">
            <thead>
            <tr>
         <th>Age</th>
         <th>Name</th>
         <th>Class</th>
         </tr>
         <tr>
            <td>45</td>
            <td>Abdul</td>
            <td>Mca</td>
         </tr>
            </thead>
        
     </table>
      </div> */}
      </div>

    );
}