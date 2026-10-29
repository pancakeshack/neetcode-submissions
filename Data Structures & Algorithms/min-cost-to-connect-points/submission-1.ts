interface Edge {
    i: number;
    j: number;
    cost: number;
}

class Solution {
    /**
     * @param {number[][]} points
     * @return {number}
     */
    minCostConnectPoints(points: number[][]): number {
        const edges: Edge[] = [];

        const n = points.length;
        for (let i = 0; i < n; i++) {
            for (let j = i + 1; j < n; j++) {
                const cost = Math.abs(points[i][0] - points[j][0])
                    + Math.abs(points[i][1] - points[j][1])
                edges.push({i: i, j: j, cost: cost});
            }
        }

        edges.sort((a: Edge, b: Edge) => (a.cost - b.cost));

        const parents = Array.from({ length: n }, (_, i) => i);

        let cost = 0;
        for (let e of edges) {
            const unioned = this.union(parents, e.i, e.j);
            if (unioned) {
                cost += e.cost;
            }
        }

        return cost;
    }

    find(parents: number[], i: number): number {
        let j = i;
        while (parents[j] != j) {
            j = parents[j];
        }

        return j;
    }

    union(parents: number[], i: number, j: number): boolean {
        const iParent = this.find(parents, i);
        const jParent = this.find(parents, j);

        if (iParent == jParent) {
            return false;
        }

        parents[iParent] = jParent;
        return true;
    }
}
