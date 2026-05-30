import Navbar from "../components/Navbar";
import MetricsPanel from "../components/MetricsPanel";
import RadarScreen from "../components/RadarScreen";
import ThreatConsole from "../components/ThreatConsole";
import TargetDetails from "../components/TargetDetails";

const Dashboard = () => {
  return (
    <div className="dashboard">

      <Navbar />

      <MetricsPanel />

      <div className="main-grid">

        <RadarScreen />

        <ThreatConsole />

      </div>

      <TargetDetails />

    </div>
  );
};

export default Dashboard;