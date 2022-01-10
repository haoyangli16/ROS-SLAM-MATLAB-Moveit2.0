<actor name='actor'>
      <skin>
        <filename>walk.dae</filename>
      </skin>
      <animation name="walking">
        <filename>walk.dae</filename>
        <interpolate_x>true</interpolate_x>
      </animation>
      <script>
        <trajectory id='0' type='walking' tension='0'>
          <waypoint>
            <time>0</time>
            <pose>9 14 0.2 0 0 -1.57</pose>
          </waypoint>
          <waypoint>
            <time>100</time>
            <pose>9 -10 0.2 0 0 -1.57</pose>
          </waypoint>
          <waypoint>
            <time>110</time>
            <pose>9 -10 0.2 0 0 1.57</pose>
          </waypoint>
          <waypoint>
            <time>210</time>
            <pose>9 14 0.2 0 0 1.57</pose>
          </waypoint>
          <waypoint>
            <time>220</time>
            <pose>9 14 0.2 0 0 -1.57</pose>
          </waypoint>
        </trajectory>
      </script>
      <link name='actor_pose'>
        <gravity>0</gravity>
        <self_collide>0</self_collide>
        <visual name='actor_visual'>
          <geometry>
            <mesh>
              <uri>walk.dae</uri>
              <scale>1 1 1</scale>
            </mesh>
          </geometry>
          <pose frame=''>0 0 0 0 -0 0</pose>
        </visual>
        <enable_wind>0</enable_wind>
      </link>
      <link name='Hips'>
        <gravity>0</gravity>
        <self_collide>0</self_collide>
        <pose frame=''>0 0 0 0 -0 0</pose>
        <inertial>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <mass>1</mass>
          <inertia>
            <ixx>4e-05</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>4e-05</iyy>
            <iyz>0</iyz>
            <izz>4e-05</izz>
          </inertia>
        </inertial>
        <visual name='Hips__SKELETON_VISUAL__'>
          <geometry>
            <sphere>
              <radius>0.02</radius>
            </sphere>
          </geometry>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>0 0 1 1</ambient>
          </material>
        </visual>
        <enable_wind>0</enable_wind>
      </link>
      <link name='LHipJoint'>
        <gravity>0</gravity>
        <self_collide>0</self_collide>
        <pose frame=''>0 0 0 -1.96446 0.68846 -2.58604</pose>
        <inertial>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <mass>1</mass>
          <inertia>
            <ixx>4e-05</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>4e-05</iyy>
            <iyz>0</iyz>
            <izz>4e-05</izz>
          </inertia>
        </inertial>
        <visual name='LHipJoint__SKELETON_VISUAL__'>
          <geometry>
            <sphere>
              <radius>0.02</radius>
            </sphere>
          </geometry>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>1 0 0 1</ambient>
          </material>
        </visual>
        <visual name='LHipJoint_LeftUpLeg__SKELETON_VISUAL__'>
          <geometry>
            <box>
              <size>0.02 0.02 0.153556</size>
            </box>
          </geometry>
          <pose frame=''>-0 0.076778 0 -1.5708 -0.436252 0</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>0 1 0 1</ambient>
          </material>
        </visual>
        <collision name='LHipJoint_LeftUpLeg_collision'>
          <geometry>
            <box>
              <size>0.02 0.02 0.153556</size>
            </box>
          </geometry>
          <pose frame=''>-0 0.076778 0 -1.5708 -0.436252 0</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <enable_wind>0</enable_wind>
      </link>
      <link name='LeftUpLeg'>
        <gravity>0</gravity>
        <self_collide>0</self_collide>
        <pose frame=''>0.045484 0.097562 -0.10951 -1.5708 -0.017454 -1.5708</pose>
        <inertial>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <mass>1</mass>
          <inertia>
            <ixx>4e-05</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>4e-05</iyy>
            <iyz>0</iyz>
            <izz>4e-05</izz>
          </inertia>
        </inertial>
        <visual name='LeftUpLeg__SKELETON_VISUAL__'>
          <geometry>
            <sphere>
              <radius>0.02</radius>
            </sphere>
          </geometry>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>1 0 0 1</ambient>
          </material>
        </visual>
        <visual name='LeftUpLeg_LeftLeg__SKELETON_VISUAL__'>
          <geometry>
            <box>
              <size>0.02 0.02 0.43615</size>
            </box>
          </geometry>
          <pose frame=''>-0 0.218075 -0 1.5708 -3e-06 -3.14159</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>0 1 0 1</ambient>
          </material>
        </visual>
        <collision name='LeftUpLeg_LeftLeg_collision'>
          <geometry>
            <box>
              <size>0.02 0.02 0.43615</size>
            </box>
          </geometry>
          <pose frame=''>-0 0.218075 -0 1.5708 -3e-06 -3.14159</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <enable_wind>0</enable_wind>
      </link>
      <link name='LeftLeg'>
        <gravity>0</gravity>
        <self_collide>0</self_collide>
        <pose frame=''>0.045484 0.08995 -0.545594 -1.5708 -0.018883 -1.5708</pose>
        <inertial>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <mass>1</mass>
          <inertia>
            <ixx>4e-05</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>4e-05</iyy>
            <iyz>0</iyz>
            <izz>4e-05</izz>
          </inertia>
        </inertial>
        <visual name='LeftLeg__SKELETON_VISUAL__'>
          <geometry>
            <sphere>
              <radius>0.02</radius>
            </sphere>
          </geometry>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>1 0 0 1</ambient>
          </material>
        </visual>
        <visual name='LeftLeg_LeftFoot__SKELETON_VISUAL__'>
          <geometry>
            <box>
              <size>0.02 0.02 0.445971</size>
            </box>
          </geometry>
          <pose frame=''>0 0.222985 -0 1.5708 -2e-06 3.14159</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>0 1 0 1</ambient>
          </material>
        </visual>
        <collision name='LeftLeg_LeftFoot_collision'>
          <geometry>
            <box>
              <size>0.02 0.02 0.445971</size>
            </box>
          </geometry>
          <pose frame=''>0 0.222985 -0 1.5708 -2e-06 3.14159</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <enable_wind>0</enable_wind>
      </link>
      <link name='LeftFoot'>
        <gravity>0</gravity>
        <self_collide>0</self_collide>
        <pose frame=''>0.045484 0.081529 -0.991485 -2.86201 -0.004819 1.5644</pose>
        <inertial>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <mass>1</mass>
          <inertia>
            <ixx>4e-05</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>4e-05</iyy>
            <iyz>0</iyz>
            <izz>4e-05</izz>
          </inertia>
        </inertial>
        <visual name='LeftFoot__SKELETON_VISUAL__'>
          <geometry>
            <sphere>
              <radius>0.02</radius>
            </sphere>
          </geometry>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>1 0 0 1</ambient>
          </material>
        </visual>
        <visual name='LeftFoot_LeftToeBase__SKELETON_VISUAL__'>
          <geometry>
            <box>
              <size>0.02 0.02 0.137078</size>
            </box>
          </geometry>
          <pose frame=''>0 0.068539 -0 1.57112 -1.56578 3.14127</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>0 1 0 1</ambient>
          </material>
        </visual>
        <collision name='LeftFoot_LeftToeBase_collision'>
          <geometry>
            <box>
              <size>0.02 0.02 0.137078</size>
            </box>
          </geometry>
          <pose frame=''>0 0.068539 -0 1.57112 -1.56578 3.14127</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <enable_wind>0</enable_wind>
      </link>
      <link name='LeftToeBase'>
        <gravity>0</gravity>
        <self_collide>0</self_collide>
        <pose frame=''>0.177238 0.080868 -1.02931 3.14159 -0 1.5708</pose>
        <inertial>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <mass>1</mass>
          <inertia>
            <ixx>4e-05</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>4e-05</iyy>
            <iyz>0</iyz>
            <izz>4e-05</izz>
          </inertia>
        </inertial>
        <visual name='LeftToeBase__SKELETON_VISUAL__'>
          <geometry>
            <sphere>
              <radius>0.02</radius>
            </sphere>
          </geometry>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>1 1 0 1</ambient>
          </material>
        </visual>
        <enable_wind>0</enable_wind>
      </link>
      <link name='RHipJoint'>
        <gravity>0</gravity>
        <self_collide>0</self_collide>
        <pose frame=''>0 0 0 -1.96446 -0.662808 -0.520328</pose>
        <inertial>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <mass>1</mass>
          <inertia>
            <ixx>4e-05</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>4e-05</iyy>
            <iyz>0</iyz>
            <izz>4e-05</izz>
          </inertia>
        </inertial>
        <visual name='RHipJoint__SKELETON_VISUAL__'>
          <geometry>
            <sphere>
              <radius>0.02</radius>
            </sphere>
          </geometry>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>1 0 0 1</ambient>
          </material>
        </visual>
        <visual name='RHipJoint_RightUpLeg__SKELETON_VISUAL__'>
          <geometry>
            <box>
              <size>0.02 0.02 0.150431</size>
            </box>
          </geometry>
          <pose frame=''>0 0.075216 0 1.5708 -0.456725 3.14159</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>0 1 0 1</ambient>
          </material>
        </visual>
        <collision name='RHipJoint_RightUpLeg_collision'>
          <geometry>
            <box>
              <size>0.02 0.02 0.150431</size>
            </box>
          </geometry>
          <pose frame=''>0 0.075216 0 1.5708 -0.456725 3.14159</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <enable_wind>0</enable_wind>
      </link>
      <link name='RightUpLeg'>
        <gravity>0</gravity>
        <self_collide>0</self_collide>
        <pose frame=''>0.045484 -0.092565 -0.10951 -1.5708 0.017454 -1.5708</pose>
        <inertial>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <mass>1</mass>
          <inertia>
            <ixx>4e-05</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>4e-05</iyy>
            <iyz>0</iyz>
            <izz>4e-05</izz>
          </inertia>
        </inertial>
        <visual name='RightUpLeg__SKELETON_VISUAL__'>
          <geometry>
            <sphere>
              <radius>0.02</radius>
            </sphere>
          </geometry>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>1 0 0 1</ambient>
          </material>
        </visual>
        <visual name='RightUpLeg_RightLeg__SKELETON_VISUAL__'>
          <geometry>
            <box>
              <size>0.02 0.02 0.441703</size>
            </box>
          </geometry>
          <pose frame=''>-0 0.220852 0 -1.5708 -2e-05 0</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>0 1 0 1</ambient>
          </material>
        </visual>
        <collision name='RightUpLeg_RightLeg_collision'>
          <geometry>
            <box>
              <size>0.02 0.02 0.441703</size>
            </box>
          </geometry>
          <pose frame=''>-0 0.220852 0 -1.5708 -2e-05 0</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <enable_wind>0</enable_wind>
      </link>
      <link name='RightLeg'>
        <gravity>0</gravity>
        <self_collide>0</self_collide>
        <pose frame=''>0.045484 -0.084856 -0.551146 -1.5708 0.018902 -1.5708</pose>
        <inertial>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <mass>1</mass>
          <inertia>
            <ixx>4e-05</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>4e-05</iyy>
            <iyz>0</iyz>
            <izz>4e-05</izz>
          </inertia>
        </inertial>
        <visual name='RightLeg__SKELETON_VISUAL__'>
          <geometry>
            <sphere>
              <radius>0.02</radius>
            </sphere>
          </geometry>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>1 0 0 1</ambient>
          </material>
        </visual>
        <visual name='RightLeg_RightFoot__SKELETON_VISUAL__'>
          <geometry>
            <box>
              <size>0.02 0.02 0.440154</size>
            </box>
          </geometry>
          <pose frame=''>-0 0.220077 -0 -1.5708 -2.9e-05 -0</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>0 1 0 1</ambient>
          </material>
        </visual>
        <collision name='RightLeg_RightFoot_collision'>
          <geometry>
            <box>
              <size>0.02 0.02 0.440154</size>
            </box>
          </geometry>
          <pose frame=''>-0 0.220077 -0 -1.5708 -2.9e-05 -0</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <enable_wind>0</enable_wind>
      </link>
      <link name='RightFoot'>
        <gravity>0</gravity>
        <self_collide>0</self_collide>
        <pose frame=''>0.045484 -0.076537 -0.991221 -2.81408 0.005615 1.57863</pose>
        <inertial>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <mass>1</mass>
          <inertia>
            <ixx>4e-05</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>4e-05</iyy>
            <iyz>0</iyz>
            <izz>4e-05</izz>
          </inertia>
        </inertial>
        <visual name='RightFoot__SKELETON_VISUAL__'>
          <geometry>
            <sphere>
              <radius>0.02</radius>
            </sphere>
          </geometry>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>1 0 0 1</ambient>
          </material>
        </visual>
        <visual name='RightFoot_RightToeBase__SKELETON_VISUAL__'>
          <geometry>
            <box>
              <size>0.02 0.02 0.145278</size>
            </box>
          </geometry>
          <pose frame=''>-0 0.072639 -0 -1.57103 -1.56487 0.000233</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>0 1 0 1</ambient>
          </material>
        </visual>
        <collision name='RightFoot_RightToeBase_collision'>
          <geometry>
            <box>
              <size>0.02 0.02 0.145278</size>
            </box>
          </geometry>
          <pose frame=''>-0 0.072639 -0 -1.57103 -1.56487 0.000233</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <enable_wind>0</enable_wind>
      </link>
      <link name='RightToeBase'>
        <gravity>0</gravity>
        <self_collide>0</self_collide>
        <pose frame=''>0.183038 -0.075721 -1.03795 3.14159 -0 1.5708</pose>
        <inertial>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <mass>1</mass>
          <inertia>
            <ixx>4e-05</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>4e-05</iyy>
            <iyz>0</iyz>
            <izz>4e-05</izz>
          </inertia>
        </inertial>
        <visual name='RightToeBase__SKELETON_VISUAL__'>
          <geometry>
            <sphere>
              <radius>0.02</radius>
            </sphere>
          </geometry>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>1 1 0 1</ambient>
          </material>
        </visual>
        <enable_wind>0</enable_wind>
      </link>
      <link name='LowerBack'>
        <gravity>0</gravity>
        <self_collide>0</self_collide>
        <pose frame=''>0 0 0 1.76781 -0.000162 1.57081</pose>
        <inertial>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <mass>1</mass>
          <inertia>
            <ixx>4e-05</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>4e-05</iyy>
            <iyz>0</iyz>
            <izz>4e-05</izz>
          </inertia>
        </inertial>
        <visual name='LowerBack__SKELETON_VISUAL__'>
          <geometry>
            <sphere>
              <radius>0.02</radius>
            </sphere>
          </geometry>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>1 0 0 1</ambient>
          </material>
        </visual>
        <visual name='LowerBack_Spine__SKELETON_VISUAL__'>
          <geometry>
            <box>
              <size>0.02 0.02 0.134285</size>
            </box>
          </geometry>
          <pose frame=''>0 0.067142 0 1.5705 -1.56997 -3.14129</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>0 1 0 1</ambient>
          </material>
        </visual>
        <collision name='LowerBack_Spine_collision'>
          <geometry>
            <box>
              <size>0.02 0.02 0.134285</size>
            </box>
          </geometry>
          <pose frame=''>0 0.067142 0 1.5705 -1.56997 -3.14129</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <enable_wind>0</enable_wind>
      </link>
      <link name='Spine'>
        <gravity>0</gravity>
        <self_collide>0</self_collide>
        <pose frame=''>0.026286 -2.1e-05 0.131687 1.55532 0.026085 1.57059</pose>
        <inertial>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <mass>1</mass>
          <inertia>
            <ixx>4e-05</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>4e-05</iyy>
            <iyz>0</iyz>
            <izz>4e-05</izz>
          </inertia>
        </inertial>
        <visual name='Spine__SKELETON_VISUAL__'>
          <geometry>
            <sphere>
              <radius>0.02</radius>
            </sphere>
          </geometry>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>1 0 0 1</ambient>
          </material>
        </visual>
        <visual name='Spine_Spine1__SKELETON_VISUAL__'>
          <geometry>
            <box>
              <size>0.02 0.02 0.132976</size>
            </box>
          </geometry>
          <pose frame=''>-0 0.066488 -0 -1.5708 0.535365 0</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>0 1 0 1</ambient>
          </material>
        </visual>
        <collision name='Spine_Spine1_collision'>
          <geometry>
            <box>
              <size>0.02 0.02 0.132976</size>
            </box>
          </geometry>
          <pose frame=''>-0 0.066488 -0 -1.5708 0.535365 0</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <enable_wind>0</enable_wind>
      </link>
      <link name='Spine1'>
        <gravity>0</gravity>
        <self_collide>0</self_collide>
        <pose frame=''>0.024228 0.003447 0.264602 1.55532 0.001964 1.57097</pose>
        <inertial>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <mass>1</mass>
          <inertia>
            <ixx>4e-05</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>4e-05</iyy>
            <iyz>0</iyz>
            <izz>4e-05</izz>
          </inertia>
        </inertial>
        <visual name='Spine1__SKELETON_VISUAL__'>
          <geometry>
            <sphere>
              <radius>0.02</radius>
            </sphere>
          </geometry>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>1 0 0 1</ambient>
          </material>
        </visual>
        <enable_wind>0</enable_wind>
      </link>
      <link name='Neck'>
        <gravity>0</gravity>
        <self_collide>0</self_collide>
        <pose frame=''>0.024228 0.003447 0.264602 1.70269 0.004587 1.57496</pose>
        <inertial>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <mass>1</mass>
          <inertia>
            <ixx>4e-05</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>4e-05</iyy>
            <iyz>0</iyz>
            <izz>4e-05</izz>
          </inertia>
        </inertial>
        <visual name='Neck__SKELETON_VISUAL__'>
          <geometry>
            <sphere>
              <radius>0.02</radius>
            </sphere>
          </geometry>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>1 0 0 1</ambient>
          </material>
        </visual>
        <visual name='Neck_Neck1__SKELETON_VISUAL__'>
          <geometry>
            <box>
              <size>0.02 0.02 0.114158</size>
            </box>
          </geometry>
          <pose frame=''>0 0.057079 -0 -1.57081 -1.53593 9e-06</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>0 1 0 1</ambient>
          </material>
        </visual>
        <collision name='Neck_Neck1_collision'>
          <geometry>
            <box>
              <size>0.02 0.02 0.114158</size>
            </box>
          </geometry>
          <pose frame=''>0 0.057079 -0 -1.57081 -1.53593 9e-06</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <enable_wind>0</enable_wind>
      </link>
      <link name='Neck1'>
        <gravity>0</gravity>
        <self_collide>0</self_collide>
        <pose frame=''>0.039239 0.004029 0.377767 1.41714 -0.001065 1.57666</pose>
        <inertial>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <mass>1</mass>
          <inertia>
            <ixx>4e-05</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>4e-05</iyy>
            <iyz>0</iyz>
            <izz>4e-05</izz>
          </inertia>
        </inertial>
        <visual name='Neck1__SKELETON_VISUAL__'>
          <geometry>
            <sphere>
              <radius>0.02</radius>
            </sphere>
          </geometry>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>1 0 0 1</ambient>
          </material>
        </visual>
        <visual name='Neck1_Head__SKELETON_VISUAL__'>
          <geometry>
            <box>
              <size>0.02 0.02 0.091751</size>
            </box>
          </geometry>
          <pose frame=''>-0 0.045875 0 1.57073 1.56383 3.14153</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>0 1 0 1</ambient>
          </material>
        </visual>
        <collision name='Neck1_Head_collision'>
          <geometry>
            <box>
              <size>0.02 0.02 0.091751</size>
            </box>
          </geometry>
          <pose frame=''>-0 0.045875 0 1.57073 1.56383 3.14153</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <enable_wind>0</enable_wind>
      </link>
      <link name='Head'>
        <gravity>0</gravity>
        <self_collide>0</self_collide>
        <pose frame=''>0.025197 0.00385 0.468437 1.50823 -4.5e-05 1.57161</pose>
        <inertial>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <mass>1</mass>
          <inertia>
            <ixx>4e-05</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>4e-05</iyy>
            <iyz>0</iyz>
            <izz>4e-05</izz>
          </inertia>
        </inertial>
        <visual name='Head__SKELETON_VISUAL__'>
          <geometry>
            <sphere>
              <radius>0.02</radius>
            </sphere>
          </geometry>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>1 1 0 1</ambient>
          </material>
        </visual>
        <enable_wind>0</enable_wind>
      </link>
      <link name='LeftShoulder'>
        <gravity>0</gravity>
        <self_collide>0</self_collide>
        <pose frame=''>0.024228 0.003447 0.264602 0.861273 1.26292 1.04166</pose>
        <inertial>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <mass>1</mass>
          <inertia>
            <ixx>4e-05</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>4e-05</iyy>
            <iyz>0</iyz>
            <izz>4e-05</izz>
          </inertia>
        </inertial>
        <visual name='LeftShoulder__SKELETON_VISUAL__'>
          <geometry>
            <sphere>
              <radius>0.02</radius>
            </sphere>
          </geometry>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>1 0 0 1</ambient>
          </material>
        </visual>
        <visual name='LeftShoulder_LeftArm__SKELETON_VISUAL__'>
          <geometry>
            <box>
              <size>0.02 0.02 0.214115</size>
            </box>
          </geometry>
          <pose frame=''>-0 0.107058 0 -1.5708 0.204274 0</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>0 1 0 1</ambient>
          </material>
        </visual>
        <collision name='LeftShoulder_LeftArm_collision'>
          <geometry>
            <box>
              <size>0.02 0.02 0.214115</size>
            </box>
          </geometry>
          <pose frame=''>-0 0.107058 0 -1.5708 0.204274 0</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <enable_wind>0</enable_wind>
      </link>
      <link name='LeftArm'>
        <gravity>0</gravity>
        <self_collide>0</self_collide>
        <pose frame=''>-0.018043 0.207494 0.313829 3e-06 1.57079 3e-06</pose>
        <inertial>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <mass>1</mass>
          <inertia>
            <ixx>4e-05</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>4e-05</iyy>
            <iyz>0</iyz>
            <izz>4e-05</izz>
          </inertia>
        </inertial>
        <visual name='LeftArm__SKELETON_VISUAL__'>
          <geometry>
            <sphere>
              <radius>0.02</radius>
            </sphere>
          </geometry>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>1 0 0 1</ambient>
          </material>
        </visual>
        <visual name='LeftArm_LeftForeArm__SKELETON_VISUAL__'>
          <geometry>
            <box>
              <size>0.02 0.02 0.319492</size>
            </box>
          </geometry>
          <pose frame=''>-0 0.159746 0 -1.5708 -0 0</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>0 1 0 1</ambient>
          </material>
        </visual>
        <collision name='LeftArm_LeftForeArm_collision'>
          <geometry>
            <box>
              <size>0.02 0.02 0.319492</size>
            </box>
          </geometry>
          <pose frame=''>-0 0.159746 0 -1.5708 -0 0</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <enable_wind>0</enable_wind>
      </link>
      <link name='LeftForeArm'>
        <gravity>0</gravity>
        <self_collide>0</self_collide>
        <pose frame=''>-0.018042 0.526986 0.313829 3e-06 1.57079 3e-06</pose>
        <inertial>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <mass>1</mass>
          <inertia>
            <ixx>4e-05</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>4e-05</iyy>
            <iyz>0</iyz>
            <izz>4e-05</izz>
          </inertia>
        </inertial>
        <visual name='LeftForeArm__SKELETON_VISUAL__'>
          <geometry>
            <sphere>
              <radius>0.02</radius>
            </sphere>
          </geometry>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>1 0 0 1</ambient>
          </material>
        </visual>
        <visual name='LeftForeArm_LeftHand__SKELETON_VISUAL__'>
          <geometry>
            <box>
              <size>0.02 0.02 0.232586</size>
            </box>
          </geometry>
          <pose frame=''>0 0.116293 -0 -1.5708 -0 -0</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>0 1 0 1</ambient>
          </material>
        </visual>
        <collision name='LeftForeArm_LeftHand_collision'>
          <geometry>
            <box>
              <size>0.02 0.02 0.232586</size>
            </box>
          </geometry>
          <pose frame=''>0 0.116293 -0 -1.5708 -0 -0</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <enable_wind>0</enable_wind>
      </link>
      <link name='LeftHand'>
        <gravity>0</gravity>
        <self_collide>0</self_collide>
        <pose frame=''>-0.018042 0.759572 0.313829 3e-06 1.57079 3e-06</pose>
        <inertial>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <mass>1</mass>
          <inertia>
            <ixx>4e-05</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>4e-05</iyy>
            <iyz>0</iyz>
            <izz>4e-05</izz>
          </inertia>
        </inertial>
        <visual name='LeftHand__SKELETON_VISUAL__'>
          <geometry>
            <sphere>
              <radius>0.02</radius>
            </sphere>
          </geometry>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>1 0 0 1</ambient>
          </material>
        </visual>
        <enable_wind>0</enable_wind>
      </link>
      <link name='LeftFingerBase'>
        <gravity>0</gravity>
        <self_collide>0</self_collide>
        <pose frame=''>-0.018042 0.759572 0.313829 3e-06 1.57079 3e-06</pose>
        <inertial>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <mass>1</mass>
          <inertia>
            <ixx>4e-05</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>4e-05</iyy>
            <iyz>0</iyz>
            <izz>4e-05</izz>
          </inertia>
        </inertial>
        <visual name='LeftFingerBase__SKELETON_VISUAL__'>
          <geometry>
            <sphere>
              <radius>0.02</radius>
            </sphere>
          </geometry>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>1 0 0 1</ambient>
          </material>
        </visual>
        <visual name='LeftFingerBase_LeftHandIndex1__SKELETON_VISUAL__'>
          <geometry>
            <box>
              <size>0.02 0.02 0.032808</size>
            </box>
          </geometry>
          <pose frame=''>0 0.016404 -0 -1.5708 -0 -0</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>0 1 0 1</ambient>
          </material>
        </visual>
        <collision name='LeftFingerBase_LeftHandIndex1_collision'>
          <geometry>
            <box>
              <size>0.02 0.02 0.032808</size>
            </box>
          </geometry>
          <pose frame=''>0 0.016404 -0 -1.5708 -0 -0</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <enable_wind>0</enable_wind>
      </link>
      <link name='LeftHandIndex1'>
        <gravity>0</gravity>
        <self_collide>0</self_collide>
        <pose frame=''>-0.018042 0.792381 0.313829 3e-06 1.57079 3e-06</pose>
        <inertial>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <mass>1</mass>
          <inertia>
            <ixx>4e-05</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>4e-05</iyy>
            <iyz>0</iyz>
            <izz>4e-05</izz>
          </inertia>
        </inertial>
        <visual name='LeftHandIndex1__SKELETON_VISUAL__'>
          <geometry>
            <sphere>
              <radius>0.02</radius>
            </sphere>
          </geometry>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>1 1 0 1</ambient>
          </material>
        </visual>
        <enable_wind>0</enable_wind>
      </link>
      <link name='LThumb'>
        <gravity>0</gravity>
        <self_collide>0</self_collide>
        <pose frame=''>-0.018043 0.759572 0.313829 -3.14159 0.785398 2.35619</pose>
        <inertial>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <mass>1</mass>
          <inertia>
            <ixx>4e-05</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>4e-05</iyy>
            <iyz>0</iyz>
            <izz>4e-05</izz>
          </inertia>
        </inertial>
        <visual name='LThumb__SKELETON_VISUAL__'>
          <geometry>
            <sphere>
              <radius>0.02</radius>
            </sphere>
          </geometry>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>1 1 0 1</ambient>
          </material>
        </visual>
        <enable_wind>0</enable_wind>
      </link>
      <link name='RightShoulder'>
        <gravity>0</gravity>
        <self_collide>0</self_collide>
        <pose frame=''>0.024228 0.003447 0.264602 1.17558 -1.21236 1.84664</pose>
        <inertial>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <mass>1</mass>
          <inertia>
            <ixx>4e-05</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>4e-05</iyy>
            <iyz>0</iyz>
            <izz>4e-05</izz>
          </inertia>
        </inertial>
        <visual name='RightShoulder__SKELETON_VISUAL__'>
          <geometry>
            <sphere>
              <radius>0.02</radius>
            </sphere>
          </geometry>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>1 0 0 1</ambient>
          </material>
        </visual>
        <visual name='RightShoulder_RightArm__SKELETON_VISUAL__'>
          <geometry>
            <box>
              <size>0.02 0.02 0.203532</size>
            </box>
          </geometry>
          <pose frame=''>0 0.101766 0 1.5708 0.143241 -3.14159</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>0 1 0 1</ambient>
          </material>
        </visual>
        <collision name='RightShoulder_RightArm_collision'>
          <geometry>
            <box>
              <size>0.02 0.02 0.203532</size>
            </box>
          </geometry>
          <pose frame=''>0 0.101766 0 1.5708 0.143241 -3.14159</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <enable_wind>0</enable_wind>
      </link>
      <link name='RightArm'>
        <gravity>0</gravity>
        <self_collide>0</self_collide>
        <pose frame=''>-0.003261 -0.18715 0.330499 0.040063 -1.57079 3.10153</pose>
        <inertial>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <mass>1</mass>
          <inertia>
            <ixx>4e-05</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>4e-05</iyy>
            <iyz>0</iyz>
            <izz>4e-05</izz>
          </inertia>
        </inertial>
        <visual name='RightArm__SKELETON_VISUAL__'>
          <geometry>
            <sphere>
              <radius>0.02</radius>
            </sphere>
          </geometry>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>1 0 0 1</ambient>
          </material>
        </visual>
        <visual name='RightArm_RightForeArm__SKELETON_VISUAL__'>
          <geometry>
            <box>
              <size>0.02 0.02 0.32836</size>
            </box>
          </geometry>
          <pose frame=''>-0 0.16418 -0 1.5708 -0 3.14159</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>0 1 0 1</ambient>
          </material>
        </visual>
        <collision name='RightArm_RightForeArm_collision'>
          <geometry>
            <box>
              <size>0.02 0.02 0.32836</size>
            </box>
          </geometry>
          <pose frame=''>-0 0.16418 -0 1.5708 -0 3.14159</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <enable_wind>0</enable_wind>
      </link>
      <link name='RightForeArm'>
        <gravity>0</gravity>
        <self_collide>0</self_collide>
        <pose frame=''>-0.003261 -0.51551 0.330499 0.042483 -1.57079 3.09911</pose>
        <inertial>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <mass>1</mass>
          <inertia>
            <ixx>4e-05</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>4e-05</iyy>
            <iyz>0</iyz>
            <izz>4e-05</izz>
          </inertia>
        </inertial>
        <visual name='RightForeArm__SKELETON_VISUAL__'>
          <geometry>
            <sphere>
              <radius>0.02</radius>
            </sphere>
          </geometry>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>1 0 0 1</ambient>
          </material>
        </visual>
        <visual name='RightForeArm_RightHand__SKELETON_VISUAL__'>
          <geometry>
            <box>
              <size>0.02 0.02 0.233209</size>
            </box>
          </geometry>
          <pose frame=''>0 0.116605 -0 1.5708 -0 3.14159</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>0 1 0 1</ambient>
          </material>
        </visual>
        <collision name='RightForeArm_RightHand_collision'>
          <geometry>
            <box>
              <size>0.02 0.02 0.233209</size>
            </box>
          </geometry>
          <pose frame=''>0 0.116605 -0 1.5708 -0 3.14159</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <enable_wind>0</enable_wind>
      </link>
      <link name='RightHand'>
        <gravity>0</gravity>
        <self_collide>0</self_collide>
        <pose frame=''>-0.003261 -0.748719 0.330499 0.042483 -1.57079 3.09911</pose>
        <inertial>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <mass>1</mass>
          <inertia>
            <ixx>4e-05</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>4e-05</iyy>
            <iyz>0</iyz>
            <izz>4e-05</izz>
          </inertia>
        </inertial>
        <visual name='RightHand__SKELETON_VISUAL__'>
          <geometry>
            <sphere>
              <radius>0.02</radius>
            </sphere>
          </geometry>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>1 0 0 1</ambient>
          </material>
        </visual>
        <enable_wind>0</enable_wind>
      </link>
      <link name='RightFingerBase'>
        <gravity>0</gravity>
        <self_collide>0</self_collide>
        <pose frame=''>-0.003261 -0.748719 0.330499 0.042483 -1.57079 3.09911</pose>
        <inertial>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <mass>1</mass>
          <inertia>
            <ixx>4e-05</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>4e-05</iyy>
            <iyz>0</iyz>
            <izz>4e-05</izz>
          </inertia>
        </inertial>
        <visual name='RightFingerBase__SKELETON_VISUAL__'>
          <geometry>
            <sphere>
              <radius>0.02</radius>
            </sphere>
          </geometry>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>1 0 0 1</ambient>
          </material>
        </visual>
        <visual name='RightFingerBase_RightHandIndex1__SKELETON_VISUAL__'>
          <geometry>
            <box>
              <size>0.02 0.02 0.046334</size>
            </box>
          </geometry>
          <pose frame=''>-0 0.023167 0 1.5708 -0 3.14159</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>0 1 0 1</ambient>
          </material>
        </visual>
        <collision name='RightFingerBase_RightHandIndex1_collision'>
          <geometry>
            <box>
              <size>0.02 0.02 0.046334</size>
            </box>
          </geometry>
          <pose frame=''>-0 0.023167 0 1.5708 -0 3.14159</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <enable_wind>0</enable_wind>
      </link>
      <link name='RightHandIndex1'>
        <gravity>0</gravity>
        <self_collide>0</self_collide>
        <pose frame=''>-0.003261 -0.795053 0.330499 0.042483 -1.57079 3.09911</pose>
        <inertial>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <mass>1</mass>
          <inertia>
            <ixx>4e-05</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>4e-05</iyy>
            <iyz>0</iyz>
            <izz>4e-05</izz>
          </inertia>
        </inertial>
        <visual name='RightHandIndex1__SKELETON_VISUAL__'>
          <geometry>
            <sphere>
              <radius>0.02</radius>
            </sphere>
          </geometry>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>1 1 0 1</ambient>
          </material>
        </visual>
        <enable_wind>0</enable_wind>
      </link>
      <link name='RThumb'>
        <gravity>0</gravity>
        <self_collide>0</self_collide>
        <pose frame=''>-0.003261 -0.748719 0.330499 3.14159 -0.785398 0.785398</pose>
        <inertial>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <mass>1</mass>
          <inertia>
            <ixx>4e-05</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>4e-05</iyy>
            <iyz>0</iyz>
            <izz>4e-05</izz>
          </inertia>
        </inertial>
        <visual name='RThumb__SKELETON_VISUAL__'>
          <geometry>
            <sphere>
              <radius>0.02</radius>
            </sphere>
          </geometry>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <material>
            <script>
              <name>__default__</name>
              <uri>__default__</uri>
            </script>
            <ambient>1 1 0 1</ambient>
          </material>
        </visual>
        <enable_wind>0</enable_wind>
      </link>
    </actor>