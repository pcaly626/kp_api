import axios from 'axios';
import 'regenerator-runtime';

export const getEndpointList = () => dispatch =>{
    axios.get('/api/list').then(
        response => dispatch({type: 'LIST_ENDPOINTS', payload: response.data.endpoints})
    )
}