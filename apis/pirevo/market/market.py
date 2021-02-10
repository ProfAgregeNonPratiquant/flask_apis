import numpy as np  


class Market():
    # Conception en cours, ce sera utilisé plus tard.
    def __init__(self, r = 0.01, n=365):
        self.r = r
        self.n = n
        self.r_n = np.exp( ( np.log( 1 + r ) )/n )
        self.assets = {'risk_free_asset': Asset(1, r, 0, n )} # Modif à faire
        # ici pour n et r

    def add_asset(self, asset_name, p, u, d, n, s_0=1):
        self.assets[asset_name] = Asset(p, u, d, n, s_0)

    def get_risk_neutral_probability(self, asset_name):
        """Compute the risk-neutral probability for this asset."""
        r = self.r
        p, u, d, n, s_0 =self.assets[asset_name].get_parameters()
        return (r - d)/(u - d)


class Asset():
    def __init__(self, p, u, d, n, s_0=1, r=0.01 ):
        self.p = p
        self.u = u
        self.d = d
        self.n = n
        self.s_0 = s_0
        self.r = r

    def get_parameters(self):
        return self.p, self.u, self.d, self.n, self.s_0

    @property
    def risk_neutral_probability(self):
        """Compute the risk-neutral probability for this asset."""
        return (self.r - self.d)/(self.u - self.d)

    @property
    def values(self):
        """Compute all the values that the asset can reach."""
        n = self.n
        s_0 = self.s_0
        S = np.zeros((n + 1, n + 1))
        for i in range(n+1):
            for j in range(i, n+1):
                S[i, j] = s_0*(1 + self.u)**(j - i)*(1 + self.d)**i
        return np.around(S, 4)

    def generate_path(self, S):
        path = [self.s_0]
        i = 0
        n = self.n
        for j in range(1, n+1):
            test = np.random.rand()
            if test > self.p:
                i += 1
            path.append(S[i, j])        
        return path

    def european_call_option_values(self, k, t):
        s = self.values
        r = self.r
        q = self.risk_neutral_probability
        c = np.zeros((t + 1, t + 1))
        for i in range(t + 1):
            c[i, t] = max(s[i, t] - k, 0)
        for j in range(t)[::-1]:
            for i in range(j + 1):
                c[i, j] = (q*c[i, j + 1] + (1 - q)*c[i + 1, j + 1])/(1 + r)
        return np.around(c, 4)
