import React from "react";
import './App.css';
import {Card} from "react-bootstrap";
import {Component} from "react";

class Home extends Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            items: []
        };
    }

    componentDidMount() {
        let apiUrl = '';
        if ('BACKEND_IP' in process.env) {
           apiUrl = `http://${process.env.BACKEND_IP}:8000`;
        } else {
            apiUrl = 'http://localhost:8000';
        }
        fetch(`${apiUrl}/news`)
            .then(res => res.json())
            .then(
                (result) => {
                    console.log(result)
                    this.setState({
                        isLoaded: true,
                        items: result.results
                    });
                },
                // Note: it's important to handle errors here
                // instead of a catch() block so that we don't swallow
                // exceptions from actual bugs in components.
                (error) => {
                    this.setState({
                        isLoaded: true,
                        error
                    });
                }
            )
    }


    render() {
        const {error, isLoaded, items} = this.state;
        if (error) {
            return <div>Error: {error.message}</div>;
        } else if (!isLoaded) {
            return <div>Loading...</div>;
        } else {
            return <div>
                {
                    items.map((item, i) =>
                        <div key={i}>
                            <Card className="bg-dark text-white">
                                <Card.Img src={item.url_to_image} alt="Card image"/>
                                <Card.ImgOverlay>
                                    <Card.Title>{item.title}</Card.Title>
                                    <Card.Text>
                                        {item.content}
                                    </Card.Text>
                                    <Card.Text>{item.published_at}</Card.Text>
                                </Card.ImgOverlay>
                            </Card>
                        </div>
                    )
                }
            </div>
        }
    }
}

export default Home;
