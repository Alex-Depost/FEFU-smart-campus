import React from 'react';
import ReactDOM from 'react-dom/client';
import Incidents from './pages/Incidents';
import {createBrowserRouter, RouterProvider} from "react-router-dom";
import Audiences from "./pages/Audiences";
import AudienceInfo from "./pages/AudienceInfo";

// send request to change normal values
// warning -> fatal
//

const router = createBrowserRouter([
    {
        path: "/incidents",
        element: <Incidents />,
        errorElement: <div>404</div>
    },
    {
        path: "/audiences",
        element: <Audiences />,
        children: [{
            path: "/audiences/:audienceId",
            element: <AudienceInfo />
        }]
    },
])

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);