import { IconPreview } from 'lib/lemon-ui/icons'
import { LemonButton, LemonButtonProps } from 'lib/lemon-ui/LemonButton'
import { urls } from 'scenes/urls'

import { Node } from '~/queries/schema'

export interface OpenEditorButtonProps extends LemonButtonProps {
    query: Node | null
}

export function OpenEditorButton({ query, ...props }: OpenEditorButtonProps): JSX.Element {
    return (
        <LemonButton
            data-attr={'open-json-editor-button'}
            type="secondary"
            status="primary-alt"
            to={query ? urls.insightNew(undefined, undefined, JSON.stringify(query)) : undefined}
            icon={<IconPreview />}
            tooltip={'Open as a new insight'}
            {...props}
        />
    )
}
