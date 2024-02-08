import React, { useState } from "react";
import categoriesData from "./categoriesData";
import { Link } from "react-router-dom"; // Import Link component

const Categories = () => {
  const [selectedCategory, setSelectedCategory] = useState("vegetables");

  const handleCategoryClick = (category) => {
    setSelectedCategory(category);
  };

  return (
    <div className="row row-cols-1 row-cols-md-3 g-4" id="cards">
      {Object.keys(categoriesData).map((categoryKey) => (
        <div className="col" key={categoryKey}>
          {/* Use Link component for navigation */}
          <Link to={`/items/${categoryKey}`} style={{ textDecoration: "none", color: "inherit" }}>
            <div className="card" onClick={() => handleCategoryClick(categoryKey)}>
              <img src={categoriesData[categoryKey].image} className="card-img-top" alt={categoriesData[categoryKey].title} />
              <div className="card-body">
                <h5 className="card-title">{categoriesData[categoryKey].title}</h5>
              </div>
            </div>
          </Link>
        </div>
      ))}
    </div>
  );
};

export default Categories;
