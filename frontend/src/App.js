import React from 'react'
import {HashRouter, Route, Link, Switch, Redirect, BrowserRouter} from 'react-router-dom'
import axios from 'axios'
import AuthorList from './components/Authors.js';
import BookList from './components/Books.js';
import AuthorBookList from './components/AuthorBooks.js';

const NotFound = ({location}) => {
    return (<div>Page not found: {location.pathname}</div>)
}

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'authors': [],
            'books': []
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/authors/')
        .then(response => {
            const authors = response.data
            this.setState( {
                'authors': authors
            })
        })
        .catch(error => console.log(error))
        axios.get('http://127.0.0.1:8000/api/books/')
        .then(response => {
            const books = response.data
            this.setState( {
                'books': books
            })
        })
        .catch(error => console.log(error))
    }

    render() {
        return (
            <div>
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li><Link to='/'>Authors</Link></li>
                            <li><Link to='/books'>Books</Link></li>
                        </ul>
                    </nav>

                    <Switch>
                        <Route path='/' exact component={() => <AuthorList authors = {this.state.authors}/>} />
                        <Route path='/books' exact component={() => <BookList books = {this.state.books}/>} />
                        <Route path='/author/:id' component={() => <AuthorBookList books = {this.state.books}/>} />
                        <Redirect from='/authors' to='/' />
                        <Route component={NotFound} />
                    </Switch>
                </BrowserRouter>
            </div>
        )
    }
}

export default App;
