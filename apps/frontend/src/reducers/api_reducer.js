
const initialState = {
    graph : [],
    endpoints: []
}

export default function(state = initialState, action) {
    switch( action.type ) {
        case 'LIST_ENDPOINTS':
            return {
                ...state,
                endpoints: action.payload
            }
        default:
            return {...state};
    }
}