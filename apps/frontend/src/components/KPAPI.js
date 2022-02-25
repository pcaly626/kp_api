import React,  { Component } from 'react';
import { getEndpointList } from '../actions/api';
import { connect } from 'react-redux';
import { Chart } from './charts';
import axios from 'axios';
import './KPAPI.css';

class KPAPI extends Component {

    state = {
        components: (<div>Waiting for Graph to be selected...</div>)
    }

    componentDidMount(){
        this.props.getList()
    }

    getGraph = async (url) =>{
        const response = await axios.get(url)
        console.log(response.data)
        const data = response.data
        this.setState({components:<Chart metaData={data.graph_meta_data} 
                                         datasetOne={data.dataset_one}
                                         datasetTwo={data.dataset_two}/>})
    }

    render(){
        let endpoints = this.props.endpoints ? this.props.endpoints : [];

      
        return (
            <div className="container">
                <div className="row">
                    <ul>
                        {endpoints.map((endpoint,index)=>(
                            <li key={index}>
                                <button onClick={
                                    () => this.getGraph(endpoint.href)}>
                                        {endpoint.name}
                                </button>
                            </li>
                        ))} 
                    </ul>
                </div>
                <div className='row'>
                    {this.state.components}
                </div>
            </div>
        )
    }
}

const mapStateToProps = ( state ) => {
    return {
        endpoints: state.api_reducer.endpoints, 
        graph: state.api_reducer.graph
    }
}

const mapDispatchToProps = ( dispatch ) => {
    return {
        getList: () => dispatch(getEndpointList())
    }
}

export default connect( mapStateToProps, mapDispatchToProps)(KPAPI);