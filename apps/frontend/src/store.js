import { createStore, applyMiddleware } from 'redux';
import rootReducer from './reducers/root_reducer';
import { composeWithDevTools } from 'redux-devtools-extension';
import thunkMiddleware from 'redux-thunk';
import loggerMiddleware from "redux-logger";

const middleware = [thunkMiddleware,loggerMiddleware];

const store = createStore(
    rootReducer,
    composeWithDevTools(applyMiddleware(...middleware))
);

export default store;