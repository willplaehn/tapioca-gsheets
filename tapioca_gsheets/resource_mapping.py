# coding: utf-8

RESOURCE_MAPPING = {
    'list_spreadsheets': {
        'resource': '/spreadsheets/private/full',
        'docs': 'https://developers.google.com/google-apps/spreadsheets/worksheets'
                '#retrieve_a_list_of_spreadsheets'
    },
    'manage_worksheets': {
        'resource': '/worksheets/{key}/private/full',
        'docs': 'https://developers.google.com/google-apps/spreadsheets/worksheets'
                '#retrieve_information_about_worksheets'
    },
    'list_feed': {
        'resource': '/list/{key}/{worksheet_id}/private/full',
        'docs': 'https://developers.google.com/google-apps/spreadsheets/data'
    },
    'cell_feed': {
        'resource': '/cells/{key}/{worksheet_id}/private/full',
        'docs': 'https://developers.google.com/google-apps/spreadsheets/data'
                '#work_with_cell-based_feeds'
    },
    'cell_feed_batch': {
        'resource': '/cells/{key}/{worksheet_id}/private/full/batch',
        'docs': 'https://developers.google.com/google-apps/spreadsheets/data'
                '#update_multiple_cells_with_a_batch_request'
    }
}
