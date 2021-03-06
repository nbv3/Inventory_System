import React from 'react'
import SearchBar from '../SearchBar'
import { Button, Grid, Row, Col } from 'react-bootstrap'
import SimpleRow from '../SimpleRow'
import TagMultiSelect from '../TagMultiSelect'

function InventoryGridHeader(props) {
	var columnContents = [
		<TagMultiSelect className="tag-multi-select absolute-bottom absolute-row" placeholder="Include tags" tagsSelected={props.tagsSelected} tagHandler={props.tagHandler}/>,
		<SearchBar className="search-bar absolute-bottom absolute-row" onUserInput={props.searchHandler}/>,
		<TagMultiSelect className="tag-multi-select absolute-bottom absolute-row" placeholder="Exclude tags" tagsSelected={props.excludeTagsSelected} tagHandler={props.excludeTagHandler}/>
	];

	return (
		<Grid fluid className="search-tag-container">
		    <Row className="relative-container">
		      <Col sm={4} className="relative-container">{columnContents[0]}</Col>
		      <Col sm={4} className="relative-container">{columnContents[1]}</Col>
		      <Col sm={4} className="relative-container">{columnContents[2]}</Col>
		    </Row>
    	</Grid>
	)
}

export default InventoryGridHeader
