import { responsiveMap } from 'antd/lib/_util/responsiveObserve'

const BREAKPOINT_MAP = Object.fromEntries(
    Object.entries(responsiveMap).map(([key, cssStatement]) => [key, parsePixelValue(cssStatement)])
)
const BREAKPOINT_VALUES = Object.values(BREAKPOINT_MAP).sort((a, b) => a - b)

export function parsePixelValue(cssStatement: string): number {
    return parseFloat(cssStatement.replace(/[^\d.]/g, ''))
}

export function getActiveBreakpointValue(): number {
    const windowWidth = window.innerWidth
    const lastMatchingBreakpoint = BREAKPOINT_VALUES.filter((value) => windowWidth >= value).pop()
    return lastMatchingBreakpoint || BREAKPOINT_VALUES[0]
}

export function getBreakpoint(breakpointKey: string): number {
    return BREAKPOINT_MAP[breakpointKey] || -1
}
