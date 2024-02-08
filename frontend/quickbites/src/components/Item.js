import React from "react";
import { useParams } from "react-router-dom"; // Import useParams hook to access URL parameters
import categoriesData from "./categoriesData";
import { Card } from "react-bootstrap";

const ItemPage = () => {
  const { category } = useParams(); // Get the category parameter from the URL

  // Check if the category exists in categoriesData
  if (!categoriesData[category]) {
    return <div>No items found for this category</div>;
  }

  return (
    <div className="row row-cols-1 row-cols-md-3 g-4">
      {categoriesData[category].items.map((item) => (
        <div key={item.id} className="col">
          <Card>
            <Card.Img variant="top" src={item.image} alt={item.name} />
            <Card.Body>
              <Card.Title>{item.name}</Card.Title>
              <Card.Text>Price: ${item.price}</Card.Text>
            </Card.Body>
          </Card>
        </div>
      ))}
    </div>
  );
};

export default ItemPage;
