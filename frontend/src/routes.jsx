import {
  HomeIcon,
  UserCircleIcon,
  TableCellsIcon,
  InformationCircleIcon,
  ServerStackIcon,
  RectangleStackIcon,
} from "@heroicons/react/24/solid";
import { Home, Profile, Tables, Notifications } from "@/pages/dashboard";
import { SignIn, SignUp } from "@/pages/auth";

const icon = {
  className: "w-5 h-5 text-inherit",
};

export const routes = [
  {
    layout: "dashboard",
    pages: [
      {
        icon: <HomeIcon {...icon} />,
        name: "dashboard",
        path: "/home",
        element: <Home />,
      },
      {
        icon: <TableCellsIcon {...icon} />,
        name: "Fachinformatiker",
        path: "/fachinformatiker",
        element: <Tables />,
      },
      {
        icon: <TableCellsIcon {...icon} />,
        name: "System Integration",
        path: "/system-integration",
        element: <Tables />,
      },
      {
        icon: <TableCellsIcon {...icon} />,
        name: "Digital Network",
        path: "/digital-network",
        element: <Tables />,
      },
      {
        icon: <TableCellsIcon {...icon} />,
        name: "Software Dev",
        path: "/software-dev",
        element: <Tables />,
      },
      {
        icon: <TableCellsIcon {...icon} />,
        name: "Data & Process Analysis",
        path: "/data",
        element: <Tables />,
      },
       // {
      //   icon: <UserCircleIcon {...icon} />,
      //   name: "profile",
      //   path: "/profile",
      //   element: <Profile />,
      // },
      // {
      //   icon: <InformationCircleIcon {...icon} />,
      //   name: "notifications",
      //   path: "/notifications",
      //   element: <Notifications />,
      // },
    ],
  },
  {
    title: "auth pages",
    layout: "auth",
    pages: [
      {
        icon: <ServerStackIcon {...icon} />,
        name: "sign in",
        path: "/sign-in",
        element: <SignIn />,
      },
      {
        icon: <RectangleStackIcon {...icon} />,
        name: "sign up",
        path: "/sign-up",
        element: <SignUp />,
      },
    ],
  },
];

export default routes;
